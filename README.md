# 🍲 Recipe API (Django)

This is the backend API for the **Recipe App**, developed using Django and Django REST Framework. It provides endpoints to manage and serve recipe content to a Flutter-based mobile frontend.

---

## 🚀 Features

- Manage recipes, ingredients, and steps
- Admin panel for easy content management
- REST API for mobile frontend integration
- SQLite database (for development)
- CORS support for mobile access
- Future-ready for authentication and reviews

---

## 🛠️ Technologies Used

- Python 3.8+
- Django 4.2
- Django REST Framework
- SQLite (default, easily swappable to PostgreSQL or MySQL)
- Pillow (for image handling)
- `django-cors-headers` for frontend integration

---

## 📦 Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/recipe_api.git
   cd recipe_api
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser (for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

---

## 🔐 Admin Panel

- Visit: `http://localhost:8000/admin`
- Use the superuser credentials to log in
- Manage recipes, ingredients, and steps via UI

---

## 📡 API Endpoints (Sample)

| Endpoint               | Method | Description                   |
|------------------------|--------|-------------------------------|
| `/api/recipes/`        | GET    | List all recipes              |
| `/api/recipes/<id>/`   | GET    | Retrieve a single recipe      |
| `/api/ingredients/`    | GET    | List all ingredients          |
| `/api/steps/`          | GET    | List all recipe steps         |

> Detailed API docs coming soon (or use Postman to explore).

---

## 🌐 CORS Support

This project includes `django-cors-headers` to allow the Flutter frontend to interact with the API. The configuration is already included in `settings.py`.

---

## 📁 Directory Structure

```
recipe_api/
├── recipes/            # App for recipe models and API
├── recipe_api/         # Project settings
├── static/             # Static files (if used)
├── media/              # Uploaded images (served in dev mode)
├── db.sqlite3          # Default database
└── manage.py
```

---

## 🔧 Environment Variables

- `DEBUG`: Should be `False` in production
- `SECRET_KEY`: Replace with a strong secret in production
- `ALLOWED_HOSTS`: Configure your domain or IP

---

## ⚙️ Deployment Tips

- Swap SQLite with PostgreSQL or MySQL
- Use Gunicorn + Nginx or host via Docker
- Serve media files correctly in production

---

## 📄 License

MIT License. Feel free to use and modify as needed.

---

## 👨‍💻 Author

Amir Mazlan  
🔗 [tiktok.com/@amirmzzzz](https://www.tiktok.com/@amirmzzzz)
