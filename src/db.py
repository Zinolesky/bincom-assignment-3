"""
Database connection management for PostgreSQL.
Uses python-dotenv to read credentials from environment or fall back to defaults.
"""
import os
import psycopg2
from psycopg2.extensions import connection
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_USER = os.getenv("DB_USER", "antispam")
DB_PASSWORD = os.getenv("DB_PASSWORD", "changeme_dev")
DB_NAME = os.getenv("DB_NAME", "bincom_db")


def get_connection() -> connection:
    """Creates and returns a connection to the PostgreSQL database."""
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME,
    )
