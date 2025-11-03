import sqlite3
from pathlib import Path
import sys

DB_PATH = "notifications.db"
MIGRATIONS_DIR = "migrations"

def get_connection():
    return sqlite3.connect(DB_PATH)

def run_migrations():
    """Применить SQL-миграции из папки migrations по порядку."""
    Path(DB_PATH).touch(exist_ok=True)
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version TEXT PRIMARY KEY
            )
        """)
        conn.commit()
        applied = set(row[0] for row in cur.execute("SELECT version FROM schema_migrations"))
        for sql_file in sorted(Path(MIGRATIONS_DIR).glob("*.sql")):
            version = sql_file.stem
            if version not in applied:
                with open(sql_file, encoding="utf-8") as f:
                    cur.executescript(f.read())
                cur.execute("INSERT INTO schema_migrations (version) VALUES (?)", (version,))
                conn.commit()

# --- USERS ---
def get_user_by_tg_id(tg_id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT user_id, tg_id, name, role FROM users WHERE tg_id=?", (tg_id,))
        return cur.fetchone()

def create_user(tg_id, name, role):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO users (tg_id, name, role) VALUES (?, ?, ?)", (tg_id, name, role))
        return cur.lastrowid

# --- MEDICINES ---
def add_medicine(user_id, name, dose, description):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO medicines (user_id, name, dose, description) VALUES (?, ?, ?, ?)",
            (user_id, name, dose, description)
        )
        return cur.lastrowid

def get_medicines(user_id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, name, dose, description FROM medicines WHERE user_id=?", (user_id,))
        return cur.fetchall()

# --- SCHEDULES ---
def add_schedule(medicine_id, user_id, weekday, time, enabled=True):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO schedules (medicine_id, user_id, weekday, time, enabled) VALUES (?, ?, ?, ?, ?)",
            (medicine_id, user_id, weekday, time, int(enabled))
        )
        return cur.lastrowid

def get_schedules(user_id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, medicine_id, weekday, time, enabled FROM schedules WHERE user_id=?",
            (user_id,)
        )
        return cur.fetchall()

# --- REMINDERS ---
def add_reminder(schedule_id, status, planned_at, actual_at=None, postponed_minutes=0, default_postpone=0):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO reminders (schedule_id, status, planned_at, actual_at, postponed_minutes, default_postpone) VALUES (?, ?, ?, ?, ?, ?)",
            (schedule_id, status, planned_at, actual_at, postponed_minutes, default_postpone)
        )
        return cur.lastrowid

def get_reminders(schedule_id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, status, planned_at, actual_at, postponed_minutes, default_postpone FROM reminders WHERE schedule_id=?",
            (schedule_id,)
        )
        return cur.fetchall()

# --- LOGS ---
def add_log(user_id, event):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO logs (user_id, event) VALUES (?, ?)",
            (user_id, event)
        )
        return cur.lastrowid

# --- Запуск миграций ---
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "migrate":
        run_migrations()
