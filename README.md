# FastAPI CATALOG Application

## Make sure to configure your .env file with your database URL before running.

## 🚀 Installation Steps

1. Clone the repository:

```
git clone https://github.com/vedang6725/TODOS.git
cd TODOS
```

2. Create a virtual environment:

```
python -m venv venv
```

3. Activate the virtual environment:

* Windows:

```
venv\Scripts\activate
```

* Mac/Linux:

```
source venv/bin/activate
```

4. Install dependencies using requirements.txt:

```
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the server using:

```
uvicorn main:app --reload
```

* `main` = your Python file name
* `app` = FastAPI instance

---

## 🌐 Access the Application

* API Base URL:

```
http://127.0.0.1:8000
```

* Interactive API Docs (Swagger UI):

```
http://127.0.0.1:8000/docs
```

---

## 🗄️ Database Design

### Table: `todos`

| Column Name | Data Type    | Description                     |
| ----------- | ------------ | ------------------------------- |
| id          | Integer (PK) | Unique ID for each task         |
| title       | String       | Title of the task               |
| description | String       | Task details                    |
| completed   | Boolean      | Status of task (True/False)     |
| created_at  | DateTime     | Timestamp when task was created |

---

## 🧠 Notes

* This project is built using FastAPI.
* Uvicorn is used as the ASGI server.
* Can be extended with databases like SQLite, PostgreSQL, etc.

---

