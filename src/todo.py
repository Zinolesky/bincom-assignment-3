"""
Task 2: Persistent PostgreSQL-backed To-Do List Application.
Supports:
- Add Task
- List Tasks
- Mark Task as Completed
- Delete Task
"""
from typing import List, Dict, Any
from src.db import get_connection


def initialize_todo_table():
    """Creates the 'todos' table if it doesn't already exist."""
    query = """
    CREATE TABLE IF NOT EXISTS todos (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        is_completed BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()


def add_todo(title: str) -> int:
    """Adds a new todo task."""
    query = "INSERT INTO todos (title) VALUES (%s) RETURNING id;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (title,))
            todo_id = cur.fetchone()[0]
        conn.commit()
    return todo_id


def get_all_todos() -> List[Dict[str, Any]]:
    """Retrieves all tasks ordered by status and creation time."""
    query = "SELECT id, title, is_completed, created_at FROM todos ORDER BY id ASC;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            return [
                {
                    "id": r[0],
                    "title": r[1],
                    "is_completed": r[2],
                    "created_at": r[3],
                }
                for r in rows
            ]


def complete_todo(todo_id: int) -> bool:
    """Marks a task as completed."""
    query = "UPDATE todos SET is_completed = TRUE WHERE id = %s;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (todo_id,))
            updated = cur.rowcount > 0
        conn.commit()
    return updated


def delete_todo(todo_id: int) -> bool:
    """Deletes a task by ID."""
    query = "DELETE FROM todos WHERE id = %s;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (todo_id,))
            deleted = cur.rowcount > 0
        conn.commit()
    return deleted
