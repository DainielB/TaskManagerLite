from uuid import UUID
from sqlite3 import IntegrityError

from src.data.db_repository import DB_Repository
from src.data.task import Task


class TaskRepository(DB_Repository):

    def get_all(self):
        conn = self._connect()
        cursor = conn.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        conn.close()

        return [self.row_to_object(row) for row in rows]

    def add(self, object):
        conn = self._connect()

        try:
            conn.execute("""
                INSERT INTO tasks (id, name, description, status, priority, kind,
                                    end_date, creation_date, project_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                str(object.id), object.name, object.description, str(object.status),
                object.priority, str(object.kind), object.end_date.toString(),
                object.creation_date.toString(), object.project_id,
            ))
            conn.commit()
        except(IntegrityError):
            print("There are no projects")
        finally:
            conn.close()

    def update(self, object):
        conn = self._connect()
        conn.execute("""
            UPDATE tasks
            SET name=?, description=?, status=?, priority=?, kind=?,
                start_date=?, end_date=?, project_id=?
            WHERE id=?
        """, (
            object.name, object.description, object.status, int(object.priority),
            object.kind, object.start_date, object.end_date,
            str(object.project_id) if object.project_id else None, str(object.id),
        ))
        conn.commit()
        conn.close()

    def delete(self, object_id):
        conn = self._connect()
        conn.execute("DELETE FROM tasks WHERE id=?", (str(object_id),))
        conn.commit()
        conn.close()

    def row_to_object(self, row):
        return Task(
            name=row["name"],
            end_date=row["end_date"],
            priority=row["priority"],
            kind=row["kind"],
            status=row["status"],
            description=row["description"],
            project_id=UUID(row["project_id"]) if row["project_id"] else None,
        )
