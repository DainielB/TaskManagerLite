import sqlite3
from uuid import UUID
from pathlib import Path

from src.data.db_repository import DB_Repository
from src.data.task import Task
from constants import DB_PATH


class TaskRepository(DB_Repository):

    def __init__(self) -> None:
        ...

    def get_all_tasks(self) -> list[Task]:
        conn = self._connect()
        cursor = conn.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        conn.close()

        return [self._row_to_task(row) for row in rows]

    def add_task(self, task: Task) -> None:
        conn = self._connect()
        conn.execute("""
            INSERT INTO tasks (id, name, description, status, priority, kind,
                                start_date, end_date, creation_date, project_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            str(task.id), task.name, task.description, task.status,
            int(task.priority), task.kind, task.start_date, task.end_date,
            task.creation_date, str(task.project_id) if task.project_id else None,
        ))
        conn.commit()
        conn.close()

    def update_task(self, task: Task) -> None:
        conn = self._connect()
        conn.execute("""
            UPDATE tasks
            SET name=?, description=?, status=?, priority=?, kind=?,
                start_date=?, end_date=?, project_id=?
            WHERE id=?
        """, (
            task.name, task.description, task.status, int(task.priority),
            task.kind, task.start_date, task.end_date,
            str(task.project_id) if task.project_id else None, str(task.id),
        ))
        conn.commit()
        conn.close()

    def delete_task(self, task_id: UUID) -> None:
        conn = self._connect()
        conn.execute("DELETE FROM tasks WHERE id=?", (str(task_id),))
        conn.commit()
        conn.close()

    def _row_to_task(self, row: sqlite3.Row) -> Task:
        return Task(
            id=UUID(row["id"]),
            name=row["name"],
            description=row["description"],
            status=row["status"],
            priority=row["priority"],
            kind=row["kind"],
            start_date=row["start_date"],
            end_date=row["end_date"],
            creation_date=row["creation_date"],
            project_id=UUID(row["project_id"]) if row["project_id"] else None,
        )
