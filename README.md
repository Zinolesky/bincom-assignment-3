# Bincom Python Assessment - Third Assignment

This repository contains complete solutions for the Bincom Python Third Assignment:
1. **Fibonacci series generator** using Python generators (`yield`).
2. **Persistent To-Do list application** stored in a PostgreSQL database.
3. **PostgreSQL database setup and full CRUD operations** (Create, Read, Update, Delete).
4. **Baby names extraction via regex** from `baby2008.html` and bulk storage into a PostgreSQL table.

---

## Project Structure

```text
bincom-assignment-3/
│
├── data/
│   └── baby2008.html           # SSA baby names HTML dataset
│
├── src/
│   ├── __init__.py
│   ├── fibonacci.py            # Task 1: Fibonacci generator & list helpers
│   ├── db.py                   # Central PostgreSQL connection management
│   ├── todo.py                 # Task 2: To-Do list operations backed by PostgreSQL
│   ├── crud.py                 # Task 3: Full CRUD operations (Students table)
│   └── baby_names_db.py        # Task 4: Regex parser & bulk database migration
│
├── tests/
│   ├── __init__.py
│   └── test_fibonacci.py       # Unit tests verifying Fibonacci generator
│
├── main.py                     # Entry point executing all 4 tasks
├── requirements.txt            # Project dependencies (psycopg2-binary, python-dotenv)
├── .env.example                # Configuration template for PostgreSQL
└── README.md
```

---

## Setup & Running

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Database
Copy `.env.example` to `.env` and configure your credentials:
```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=antispam
DB_PASSWORD=changeme_dev
DB_NAME=bincom_db
```

### 3. Run All Tasks
```bash
python main.py
```

### 4. Run Unit Tests
```bash
python -m unittest discover -s tests
```
