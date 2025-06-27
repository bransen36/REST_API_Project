# Django REST API — Code Snippets

This is a simple RESTful API built using **Django** and **Django REST Framework**. It allows users to create, view, update, and delete code snippets. 

### 🔒 Permissions Overview

- ✅ **Any user** (authenticated or not) can view all code snippets.
- ✍️ **Authenticated users only** can create new snippets.
- ✏️ **Only the author** of a snippet can update or delete it.

---

## 🚀 Setup Instructions
### 1. Clone the Repository

```bash
  git clone https://github.com/bransen36/REST_API_Project.git
  cd REST_API_Project
```

### 2. Create and Activate a Virtual Environment

```bash
  python -m venv venv
  venv\Scripts\activate # On Linux: source venv/bin/activate
```

### 3. Install Dependencies

```bash
  pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
  python manage.py migrate
```

### 5. Create a Superuser (optional but recommended)

```bash
  python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
  python manage.py runserver
```
Navigate to **http://127.0.0.1:8000/snippets/** or **http://localhost:8000/snippets/** to view the API in the browser
