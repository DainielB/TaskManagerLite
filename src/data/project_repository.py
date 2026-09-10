from uuid import UUID

from src.data.db_repository import DB_Repository
from src.data.project import Project


class ProjectRepository(DB_Repository):

    def get_all(self) -> list[Project]:
        conn = self._connect()
        cursor = conn.execute("SELECT * FROM projects")
        rows = cursor.fetchall()
        conn.close()

        return [self.row_to_object(row) for row in rows]

    def add(self, object: Project) -> None:
        conn = self._connect()
        conn.execute("""
            INSERT INTO projects (id, name, description,  end_date, creation_date)
            VALUES (?, ?, ?, ?, ?)
        """, (
            str(object.id), object.name, object.description, object.end_date.toString(), object.creation_date.toString()
        ))
        conn.commit()
        conn.close()

    def update(self, object: Project) -> None:
        conn = self._connect()
        conn.execute("""
            UPDATE projects
            SET name=?, description=?, start_date=?, end_date=?
            WHERE id=?
        """, (
            object.name, object.description, object.start_date, object.end_date
        ))
        conn.commit()
        conn.close()

    def delete(self, object_id: UUID) -> None:
        conn = self._connect()
        conn.execute("DELETE FROM projects WHERE id=?", (str(object_id),))
        conn.commit()
        conn.close()

    def row_to_object(self, row) -> Project:
        return Project(
                    name=row["name"],
                    end_date=row["end_date"],
                    description=row["description"],
                )