import sqlite3

from constants import DB_PATH


def init_db() -> None:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            start_date DATE,
            end_date DATE,
            description TEXT,
            creation_date DATE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL,
            priority TEXT NOT NULL,
            kind TEXT,
            start_date TEXT,
            end_date TEXT,
            creation_date TEXT,
            project_id TEXT,
            FOREIGN KEY (project_id) REFERENCES projects(id)
        )
    """
    )

    conn.commit()
    conn.close()
