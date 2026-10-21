"""
Task 3: PostgreSQL Database Setup and Full CRUD Operations
Manages an example 'products' or 'users' entity to demonstrate:
- Create (INSERT)
- Read (SELECT)
- Update (UPDATE)
- Delete (DELETE)
"""
from typing import List, Dict, Any, Optional
from src.db import get_connection


def create_crud_table():
    """Initializes the demo 'students' table in PostgreSQL."""
    query = """
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        track VARCHAR(50) NOT NULL,
        email VARCHAR(120) UNIQUE NOT NULL,
        score INT DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()


def create_student(name: str, track: str, email: str, score: int = 0) -> int:
    """CREATE: Inserts a new student and returns the generated ID."""
    query = """
    INSERT INTO students (name, track, email, score)
    VALUES (%s, %s, %s, %s)
    RETURNING id;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (name, track, email, score))
            new_id = cur.fetchone()[0]
        conn.commit()
    return new_id


def get_all_students() -> List[Dict[str, Any]]:
    """READ: Fetches all students."""
    query = "SELECT id, name, track, email, score, created_at FROM students ORDER BY id;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            return [
                {
                    "id": r[0],
                    "name": r[1],
                    "track": r[2],
                    "email": r[3],
                    "score": r[4],
                    "created_at": r[5],
                }
                for r in rows
            ]


def get_student_by_id(student_id: int) -> Optional[Dict[str, Any]]:
    """READ: Fetches a single student by ID."""
    query = "SELECT id, name, track, email, score, created_at FROM students WHERE id = %s;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (student_id,))
            row = cur.fetchone()
            if not row:
                return None
            return {
                "id": row[0],
                "name": row[1],
                "track": row[2],
                "email": row[3],
                "score": row[4],
                "created_at": row[5],
            }


def update_student_score(student_id: int, new_score: int) -> bool:
    """UPDATE: Updates a student's score."""
    query = "UPDATE students SET score = %s WHERE id = %s;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (new_score, student_id))
            updated = cur.rowcount > 0
        conn.commit()
    return updated


def delete_student(student_id: int) -> bool:
    """DELETE: Deletes a student by ID."""
    query = "DELETE FROM students WHERE id = %s;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (student_id,))
            deleted = cur.rowcount > 0
        conn.commit()
    return deleted
