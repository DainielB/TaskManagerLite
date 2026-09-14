from uuid import UUID
from sqlite3 import IntegrityError, OperationalError

from src.data.db_repository import DB_Repository
from src.data.task import Task
from constants import DATE_FORMAT


class TaskRepository(DB_Repository):

    def get_all(self):

        try:
            with self._connect() as conn:
                cursor = conn.execute("SELECT * FROM tasks")
                rows = cursor.fetchall()
        
                return [self.row_to_object(row) for row in rows]
        except OperationalError as oe: # MODIDY THIS
            print(oe)        

    def add(self, object):
        try:
            with self._connect() as conn:        
                conn.execute("""
                    INSERT INTO tasks (id, name, description, status, priority, kind,
                                        end_date, creation_date, project_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    str(object.id), object.name, object.description, str(object.status),
                    object.priority, str(object.kind), object.end_date,
                    object.creation_date, object.project_id,
                ))
                conn.commit()
        except(IntegrityError):
            print("There are no projects")

    def update(self, object):

        try:

            with self._connect() as conn:
                conn.execute("""
                    UPDATE tasks
                    SET name=?, description=?, status=?, priority=?, kind=?,
                        start_date=?, end_date=?, project_id=?
                    WHERE id=?
                """, (
                    object.name, object.description, object.status, object.priority,
                    object.kind, object.start_date, object.end_date,
                    object.project_id if object.project_id else None, object.id,
                ))
                conn.commit()
        except OperationalError as oe:
            print(oe)

    def delete(self, object_id):

        try:
            with self._connect() as conn:
                conn.execute("DELETE FROM tasks WHERE id=?", (str(object_id),))
                conn.commit()
        except OperationalError as oe: # MODIFY THIS
            print(oe)

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