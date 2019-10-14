# Blitz-App
# Các thư viện cần cài đặt:
- Nếu chưa cài pip, thì cài theo link [PIP](https://pip.pypa.io/en/stable/installing/)
- Sau khi cài pip xong tiến hành cài đặt các thư viện:
    + pip install flask 
    + pip install flask-restful
- Sau khi cài hoàn tất các thư viện trên thì tiến hành chạy thử:
    + Vào đường dẫn thư mục của project và gõ lệnh: flask run

# Link tài liệu:
[Flask](http://flask.palletsprojects.com/en/1.1.x/)
[Flask RestFul](https://flask-restful.readthedocs.io/en/latest/)

# Mô tả cấu trúc project:
+ File app.py: dùng để start app, không chỉnh sửa trong file này
+ Thư mục model: dùng để tạo schema theo từng bảng cho database
+ Thư mục controller: dùng để xử lý logic các request
+ Thư mục access: dùng để tương tác dữ liệu với database như: select, insert, update....
+ Thư mục config: trong thư mục này dùng để tạo cái biến môi trường như: SECRET KEY, API KEY... và khởi tạo routing cho từng controller