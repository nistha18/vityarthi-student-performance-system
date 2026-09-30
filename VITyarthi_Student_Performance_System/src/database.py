import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "student_performance.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def initialize_database():
    with get_connection() as conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            reg_no TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            branch TEXT NOT NULL,
            semester INTEGER NOT NULL CHECK(semester > 0)
        );

        CREATE TABLE IF NOT EXISTS marks (
            mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            marks REAL NOT NULL CHECK(marks >= 0 AND marks <= 100),
            FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS attendance (
            attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            attended INTEGER NOT NULL CHECK(attended >= 0),
            total INTEGER NOT NULL CHECK(total > 0),
            FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE,
            CHECK(attended <= total)
        );
        """)

def fetch_all(query, params=()):
    with get_connection() as conn:
        return conn.execute(query, params).fetchall()

def execute(query, params=()):
    with get_connection() as conn:
        cur = conn.execute(query, params)
        conn.commit()
        return cur.lastrowid
