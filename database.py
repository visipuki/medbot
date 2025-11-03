import sqlite3
from pathlib import Path

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "migrate":
        run_migrations()

DB_PATH = "medication_bot.db"
MIGRATIONS_DIR = "migrations"

def get_connection():
    return sqlite3.connect(DB_PATH)

def run_migrations():
    """Apply SQL migration files in sorted order."""
    Path(DB_PATH).touch(exist_ok=True)
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version TEXT PRIMARY KEY
            )
        """)
        conn.commit()
        applied = {row[0] for row in cur.execute("SELECT version FROM schema_migrations")}
        for sql_file in sorted(Path(MIGRATIONS_DIR).glob("*.sql")):
            version = sql_file.stem
            if version not in applied:
                with open(sql_file, "r", encoding="utf-8") as f:
                    cur.executescript(f.read())
                cur.execute("INSERT INTO schema_migrations (version) VALUES (?)", (version,))
                conn.commit()

