"""
Task 4: Regex Parsing of baby2008.html and Bulk Storage into PostgreSQL.
"""
import re
from typing import List, Tuple
from psycopg2.extras import execute_values
from src.db import get_connection


def initialize_baby_names_table():
    """Creates the baby_names table in PostgreSQL."""
    query = """
    CREATE TABLE IF NOT EXISTS baby_names (
        id SERIAL PRIMARY KEY,
        rank INT NOT NULL,
        boy_name VARCHAR(50) NOT NULL,
        girl_name VARCHAR(50) NOT NULL
    );
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()


def extract_names_from_html(file_path: str) -> List[Tuple[int, str, str]]:
    """
    Extracts rank, boy name, and girl name using regular expressions.
    Pattern matches: <tr align="right"><td>1</td><td>Michael</td><td>Emma</td>
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r'<tr align="right"><td>(\d+)</td><td>([A-Za-z]+)</td><td>([A-Za-z]+)</td>'
    matches = re.findall(pattern, content)
    return [(int(rank), boy, girl) for rank, boy, girl in matches]


def save_baby_names_to_db(records: List[Tuple[int, str, str]]) -> int:
    """
    Inserts extracted baby names into the PostgreSQL table efficiently using execute_values.
    Clears existing records before inserting to keep dataset clean.
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("TRUNCATE TABLE baby_names;")
            insert_query = """
            INSERT INTO baby_names (rank, boy_name, girl_name)
            VALUES %s;
            """
            execute_values(cur, insert_query, records)
        conn.commit()
    return len(records)


def get_total_baby_names_count() -> int:
    """Returns the total number of rows in baby_names table."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM baby_names;")
            return cur.fetchone()[0]


def get_top_baby_names(limit: int = 5) -> List[Tuple]:
    """Returns the top N ranks from baby_names table."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT rank, boy_name, girl_name FROM baby_names ORDER BY rank ASC LIMIT %s;",
                (limit,),
            )
            return cur.fetchall()
