from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

app = FastAPI()

# Model

class Todo(BaseModel):
    id: int
    title: str = Field(..., min_length=3, max_length=100)
    is_done: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Fake Database (RAM)

todos: List[Todo] = []


# Create Todo

@app.post("/todos", response_model=List[Todo])
def create_todos(new_todos: List[Todo]):
    todos.extend(new_todos)
    return new_todos


# Get Todos (Filter + Search + Sort + Pagination)

@app.get("/todos")
def get_todos(
    is_done: Optional[bool] = None,
    q: Optional[str] = None,
    sort: Optional[str] = None,
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0)
):
    results = todos

    # Filter theo is_done
    if is_done is not None:
        results = [t for t in results if t.is_done == is_done]

    # Search theo title
    if q:
        results = [t for t in results if q.lower() in t.title.lower()]

    # Sort theo created_at
    if sort:
        reverse = False
        if sort.startswith("-"):
            reverse = True
            sort = sort[1:]

        if sort == "created_at":
            results = sorted(results, key=lambda x: x.created_at, reverse=reverse)

    total = len(results)

    # Pagination
    results = results[offset: offset + limit]

    return {
        "items": results,
        "total": total,
        "limit": limit,
        "offset": offset
    }
