# 🚀 Django Blog API Project

## 📌 Project Description

This is a **Django-based Blog Application** with REST API support using Django REST Framework (DRF).
The project allows users to create, read, update, and delete blog posts with authentication support.

It is designed as a **beginner-to-intermediate level backend project** to understand real-world development concepts.

---

## ✨ Features

* 📝 Create, Read, Update, Delete (CRUD) Blog Posts
* 🔐 User Authentication (Login, Signup, Logout)
* 🔑 JWT Authentication (Secure API Access)
* 📡 RESTful API using Django REST Framework
* 🧑 Admin Panel for managing data
* ⚙️ Clean and scalable project structure

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **API:** Django REST Framework (DRF)
* **Database:** SQLite / PostgreSQL
* **Authentication:** JWT (JSON Web Token)
* **Tools:** Git, GitHub

---

## 📂 Project Structure

```
blog_project/
│
├── blog/                # Main app
├── users/               # Authentication app
├── blog_project/        # Project settings
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/django-blog-api.git
cd django-blog-api
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv myvenv
```

### 3️⃣ Activate Virtual Environment

```bash
myvenv\Scripts\activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Run Server

```bash
python manage.py runserver
```

---

## 📡 API Endpoints

### 🔐 Authentication

* `POST /api/signup/` → Register user
* `POST /api/login/` → Login user
* `POST /api/logout/` → Logout user

### 📝 Blog APIs

* `GET /api/blog/` → Get all blogs
* `POST /api/blog/` → Create blog
* `GET /api/blog/{id}/` → Get single blog
* `PUT /api/blog/{id}/` → Update blog
* `DELETE /api/blog/{id}/` → Delete blog

---

## 🔑 JWT Authentication Flow

1. User logs in → gets access token
2. Token is sent in headers
3. Server verifies token for each request

Example:

```
Authorization: Bearer your_token_here
```

---

## 🧪 Testing

You can test APIs using:

* Postman
* Thunder Client (VS Code Extension)

---

## 🔒 Environment Variables

Create a `.env` file in root directory:

```
SECRET_KEY=your_secret_key
DEBUG=True
```

---

## 🚀 Deployment

You can deploy this project on:

* Render
* Railway
* PythonAnywhere

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 👤 Author

**Aniket Gupta**

---

## 📄 License

This project is open-source and free to use.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
