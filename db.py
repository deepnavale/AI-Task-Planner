import sqlite3
from datetime import datetime

# Database file name
DB_FILE = "planner.db"

def init_db():
    """Initializes the database and creates the 'plans' table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            goal TEXT NOT NULL,
            plan TEXT NOT NULL,
            timestamp DATETIME NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_plan(goal: str, plan: str):
    """Adds a new goal and its generated plan to the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    timestamp = datetime.now()
    cursor.execute(
        "INSERT INTO plans (goal, plan, timestamp) VALUES (?, ?, ?)",
        (goal, plan, timestamp)
    )
    conn.commit()
    conn.close()

def get_all_plans():
    """Retrieves all plans from the database, ordered by the most recent."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, goal, plan, timestamp FROM plans ORDER BY timestamp DESC")
    plans = cursor.fetchall()
    conn.close()
    return plans