import psycopg2

from config import load_config


def init_db() -> None:

    commands = (
        """
        CREATE TABLE IF NOT EXISTS projects (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            start_date TEXT,
            end_date TEXT NOT NULL,
            description TEXT,
            creation_date TEXT
        )
        """,
        """
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
            project_id TEXT NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE INDEX IF NOT EXISTS index_tasks_project_id ON tasks(project_id)
        """
    )


    config = load_config()

    conn = psycopg2.connect(**config)
    try:
        # with psycopg2.connect(**config) as conn:
        with conn.cursor() as cursor:
            for command in commands:
                cursor.execute(command)

        conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        conn.rollback()
        print(error)
        raise
    finally:
        conn.close()
