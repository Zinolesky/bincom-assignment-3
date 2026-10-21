"""
Master Runner for Bincom Python Assessment - Third Assignment.

Executes and demonstrates all 4 requirements:
1. Fibonacci Series Generator
2. PostgreSQL-backed To-Do List Application
3. PostgreSQL Database Table Creation & CRUD Operations
4. Extraction of Baby Names via Regex and Storage into PostgreSQL Table
"""
import os
import sys

# Ensure src is on python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.fibonacci import get_fibonacci_sequence, fibonacci_generator
from src.todo import initialize_todo_table, add_todo, get_all_todos, complete_todo, delete_todo
from src.crud import (
    create_crud_table,
    create_student,
    get_all_students,
    get_student_by_id,
    update_student_score,
    delete_student,
)
from src.baby_names_db import (
    initialize_baby_names_table,
    extract_names_from_html,
    save_baby_names_to_db,
    get_total_baby_names_count,
    get_top_baby_names,
)


def run_all_tasks():
    print("=" * 65)
    print("BINCOM PYTHON ASSESSMENT - THIRD ASSIGNMENT")
    print("=" * 65)

    # -----------------------------------------------------------------
    # TASK 1: Fibonacci Series Generator
    # -----------------------------------------------------------------
    print("\n[TASK 1] FIBONACCI SERIES GENERATOR")
    print("-" * 65)
    first_15 = get_fibonacci_sequence(15)
    print(f"First 15 Fibonacci numbers: {first_15}")

    print("Demonstrating custom generator consumption with next():")
    gen = fibonacci_generator()
    first_5_gen = [next(gen) for _ in range(5)]
    print(f"Yielded first 5 terms: {first_5_gen}")

    # -----------------------------------------------------------------
    # TASK 2: PostgreSQL-backed To-Do List
    # -----------------------------------------------------------------
    print("\n[TASK 2] POSTGRESQL TO-DO LIST APPLICATION")
    print("-" * 65)
    initialize_todo_table()
    
    t1 = add_todo("Submit Bincom Second Assignment on Google Docs")
    t2 = add_todo("Complete Third Assignment: Postgres & Python")
    t3 = add_todo("Review Algorithms & Data Structures")
    print(f"Added tasks with IDs: {t1}, {t2}, {t3}")

    complete_todo(t1)
    print(f"Completed Task ID {t1} -> Marked as Completed")

    todos = get_all_todos()
    print("Current To-Do List:")
    for item in todos:
        status = "[DONE]" if item["is_completed"] else "[PENDING]"
        print(f"  {status} ID {item['id']}: {item['title']}")

    # -----------------------------------------------------------------
    # TASK 3: PostgreSQL Database Setup and CRUD Operations
    # -----------------------------------------------------------------
    print("\n[TASK 3] POSTGRESQL DATABASE CRUD OPERATIONS")
    print("-" * 65)
    create_crud_table()

    # 1. CREATE
    s_id = create_student(
        name="Efezino Prince Taigbenu",
        track="Python Backend Development",
        email="efezino.taigbenu@example.com",
        score=85,
    )
    print(f"[CREATE] Inserted student with ID: {s_id}")

    # 2. READ
    student = get_student_by_id(s_id)
    print(f"[READ] Fetched student: {student['name']} | Track: {student['track']} | Score: {student['score']}")

    # 3. UPDATE
    update_student_score(s_id, 98)
    updated_student = get_student_by_id(s_id)
    print(f"[UPDATE] Updated score to: {updated_student['score']}")

    # 4. DELETE demo
    temp_id = create_student(
        name="Temporary Record",
        track="DevOps",
        email="temp.record@example.com",
        score=50,
    )
    deleted = delete_student(temp_id)
    print(f"[DELETE] Deleted temporary record (ID: {temp_id}) -> Success: {deleted}")

    # -----------------------------------------------------------------
    # TASK 4: Regex Extraction & Saving Baby Names to PostgreSQL
    # -----------------------------------------------------------------
    print("\n[TASK 4] REGEX BABY NAMES EXTRACTION & POSTGRESQL STORAGE")
    print("-" * 65)
    initialize_baby_names_table()

    html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "baby2008.html")
    if not os.path.exists(html_file):
        print(f"Error: {html_file} does not exist.")
        return

    extracted_records = extract_names_from_html(html_file)
    print(f"Regex extracted {len(extracted_records)} table rows (Rank, Boy Name, Girl Name).")

    inserted_count = save_baby_names_to_db(extracted_records)
    print(f"Successfully saved {inserted_count} records into PostgreSQL 'baby_names' table.")

    total_in_db = get_total_baby_names_count()
    print(f"Total rows currently in 'baby_names' table: {total_in_db}")

    print("Top 5 Baby Names in Database:")
    top_5 = get_top_baby_names(5)
    for rank, boy, girl in top_5:
        print(f"  Rank {rank}: Boy -> {boy} | Girl -> {girl}")

    print("\n" + "=" * 65)
    print("ALL 4 TASKS EXECUTED SUCCESSFULLY!")
    print("=" * 65)


if __name__ == "__main__":
    run_all_tasks()
