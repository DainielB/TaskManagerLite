from uuid import UUID

from src.data.db_repository import DB_Repository
from src.data.project import Project


class ProjectRepository(DB_Repository):

    def __init__(self) -> None:
        ...

    def get_all(self) -> list[Project]:
        # return super().get_all()

        conn = self._connect()
        cursor = conn.execute("SELECT * FROM projects")
        rows = cursor.fetchall()
        conn.close()

        return [self._row_to_project(row) for row in rows]

    def add(self, object: Project) -> None:
        # return super().add(object)

        conn = self._connect()
        conn.execute("""
            INSERT INTO projects (id, name, description, status, priority, kind,
                                start_date, end_date, creation_date, project_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            str(object.id), object.name, object.description, object.status,
            int(object.priority), object.kind, object.start_date, object.end_date,
            object.creation_date, str(object.project_id) if object.project_id else None,
        ))
        conn.commit()
        conn.close()

    def update(self, object: Project) -> None:
        # return super().update(object)

        conn = self._connect()
        conn.execute("""
            UPDATE projects
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

    def delete(self, object_id: UUID) -> None:
        # return super().delete(object_id)

        conn = self._connect()
        conn.execute("DELETE FROM projects WHERE id=?", (str(object_id),))
        conn.commit()
        conn.close()

    def row_to_object(self, row) -> Project:
        # return super().row_to_object(row)

        return Project(
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