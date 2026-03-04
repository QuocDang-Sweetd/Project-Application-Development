from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Model cho Task
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

# Giả lập database bằng list
tasks = []

@app.get("/")
def root():
    return {"message": "Welcome to To-Do API"}

@app.get("/health")
def health_check():
    return {"status": "OK"}

# Lấy tất cả task
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Tạo task mới
@app.post("/tasks/bulk", response_model=List[Task])
def create_tasks_bulk(new_tasks: List[Task]):
    tasks.extend(new_tasks)
    return new_tasks

# Lấy 1 task theo id
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Xoá task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
