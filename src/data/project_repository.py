from sqlite3 import IntegrityError, OperationalError

from src.data.db_repository import DB_Repository
from src.data.project import Project
from constants import DATE_FORMAT


class ProjectRepository(DB_Repository):

    def get_all(self) -> list[Project]:

        try:
            with self._connect() as conn:
                cursor = conn.execute("SELECT * FROM projects")
                rows = cursor.fetchall()
        
                return [self.row_to_object(row) for row in rows]
        except OperationalError as oe: # TODO: Modify the exception
            print(oe)
        else:
            return []

    def add(self, object: Project) -> None:

        try:
            with self._connect() as conn:
                conn.execute("""
                    INSERT INTO projects (id, name, description,  end_date, creation_date)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    str(object.id), object.name, object.description, object.end_date, object.creation_date
                ))
                conn.commit()
        except OperationalError as oe: # TODO: Modify the exception
            print(oe)

    def update(self, object: Project) -> None:

        try:
            with self._connect() as conn:
                conn.execute("""
                    UPDATE projects
                    SET name=?, description=?, start_date=?, end_date=?
                    WHERE id=?
                """, (
                    object.name, object.description, object.start_date, object.end_date,
                ))
                conn.commit()
        except OperationalError as oe:
            print(oe)

    def delete(self, object_id: str) -> None:

        try:
            with self._connect() as conn:
                conn.execute("DELETE FROM projects WHERE id=?", (object_id,))
                conn.commit()
        except OperationalError as oe: # MODIFY THIS
            print(oe)

    def row_to_object(self, row) -> Project:
        return Project (
            name=row["name"],
            end_date=row["end_date"],
            description=row["description"],
            id=row["id"]
        )

    def delete_tasks_by_project_id(self, project_id: str) -> None:

        try:
            with self._connect() as conn:
                conn.execute("DELETE FROM tasks WHERE project_id=?", (project_id,))
                conn.commit()
        except OperationalError as oe: # MODIFY THIS
            print(oe)