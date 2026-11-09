import sqlite3
from pathlib import Path


DB_PATH = Path("data/chemledger.db")

def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH)

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS experiments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                file_path TEXT NOT NULL,
                sha256 TEXT NOT NULL,
                signature BLOB NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )    
                """)
        connection.commit()
    finally:
        connection.close()