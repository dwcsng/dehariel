# Du ký Barber - Website Đặt Lịch Cắt Tóc

Website đặt lịch cắt tóc trực tuyến cho tiệm Du ký Barber, giúp khách hàng chủ động chọn thợ, dịch vụ, thời gian và nhận thông báo nhắc lịch.

---

## Tính năng nổi bật

- Đăng ký, đăng nhập, đăng xuất tài khoản
- Xem danh sách dịch vụ và thợ cắt tóc
- Đặt lịch cắt tóc: chọn thợ, dịch vụ, ngày giờ, ghi chú
- Xem, lọc, chỉnh sửa, hủy lịch hẹn của bạn
- Tìm kiếm dịch vụ trên trang chủ
- Giao diện hiện đại, responsive, hỗ trợ dark mode
- Thông báo email khi lịch hẹn sắp đến hạn

---

## Cài đặt & chạy thử

### 1. Clone project

```sh
git clone https://github.com/yourusername/barberproject.git
cd barberproject
```

### 2. Tạo môi trường ảo & cài đặt thư viện

```sh
python -m venv venv
source venv/bin/activate  # hoặc venv\Scripts\activate trên Windows
pip install -r requirements.txt
```

### 3. Khởi tạo database & tài khoản admin

```sh
python manage.py migrate
python manage.py createsuperuser
```

### 4. Chạy server

```sh
python manage.py runserver
```

Truy cập [http://127.0.0.1:8000/](http://127.0.0.1:8000/) để sử dụng ứng dụng.

---

## Cấu hình gửi email (tùy chọn)

Sửa file `barberproject/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

---

## Cấu trúc thư mục

```
manage.py
requirements.txt
barberproject/
    db.sqlite3
    barberproject/
        settings.py, urls.py, ...
    media/
        barbers/
        services/
    static/
        main/
main/
    models.py, views.py, forms.py, urls.py, ...
    migrations/
    templates/
        main/
            base.html, home.html, signup.html, login.html, ...
```

---

## Đóng góp

Mọi đóng góp, báo lỗi hoặc ý tưởng mới đều được hoan nghênh!  
Liên hệ: [Du ký Barber Facebook](https://www.facebook.com/profile.php?id=61576335577676)

---

**© 2024 Du ký Barber**# dehariel
