# Tên: Nguyễn Quốc Đăng
# Mã sinh viên: 23716711 
# Project: Bài tập to-do-list

- Bài làm của em được thực hiện bởi chính em và có sự hỗ trợ bởi AI
- Mô tả : Tổng quan bài làm có 8 cấp độ, ở mỗi cấp độ cấu trúc của cây sẽ khác nhau em cập nhật lại cấu trúc của bài qua 8 file trong đó có 3 file 
main.py cho cấp 0 đến 2 và kể từ cấp 3 trở đi là file .rar do cấu trúc phức tạp hơn

- Quá trình thực hiện :
  - Cấp 0: Làm quen FastAPI (Hello To-Do)
    => Chạy uvicorn và gọi được 2 endpoint.
  - Cấp 1: CRUD cơ bản (dữ liệu trong RAM)
    => đã chạy được Validate dữ liệu bằng Pydantic, trả lỗi đúng khi không tìm thấy (404)
  - Cấp 2: Validation “xịn” + filter/sort/pagination
    => chạy được Response có cấu trúc: { "items": [...], "total": 123, "limit": 10, "offset": 0 }
  - Cấp 3: Tách tầng (router/service/repository) + cấu hình chuẩn
    => chạy được FasstAPI với Không viết logic DB trong router, có file main.py sạch
  - Cấp 4: Dùng Database (SQLite/PostgreSQL) + ORM
    => Chạy được FastAPI với created_at/updated_at tự cập nhật, query có pagination thực sự từ DB
  - Cấp 5: Authentication + User riêng
    => User A không xem/xóa todo của User B, password hash bằng passlib/bcrypt
  - Cấp 6: Nâng cao (tag, deadline, nhắc việc)
    => thêm được : due_date (deadline), tags (nhiều tag), GET /todos/overdue danh sách quá hạn, GET /todos/today việc cần làm hôm nay
  - Cấp 7: Testing + tài liệu + deploy
    =>  test bằng pytes và chạy được FastAPI trên docker
  - Cấp 8: Thêm một số tính năng
    => Thêm một số tính năng như xóa, tìm kiếm, sắp xếp.
  
 
