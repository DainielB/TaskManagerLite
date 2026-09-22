import psycopg2

from src.data.db_repository import DB_Repository
from src.data.task import Task
from constants import DATE_FORMAT
from config import load_config


class TaskRepository(DB_Repository):

    def get_all(self, object_id: str = None) -> list[Task]:
        """_summary_

        Args:
            object_id (str, optional): _description_. Defaults to None.

        Returns:
            list[Task]: _description_
        """

        config = load_config()

        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:

                    if object_id:
                        query = "SELECT * FROM tasks WHERE project_id=%s"
                        cursor.execute(query, (object_id,))
                    else:
                        query = "SELECT * FROM tasks"
                        cursor.execute(query)

                    rows = cursor.fetchmany()
        
                    return [self.row_to_object(row) for row in rows]
        except psycopg2.ProgrammingError as error:
            print(error)
        finally:
            conn.close()
            return []

    def add(self, object) -> None:

        query = """
                INSERT INTO tasks (id, name, description, status, priority, 
                kind, end_date, creation_date, project_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """

        config = load_config()

        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cursor:   
                    cursor.execute(query,
                        (str(object.id), object.name, object.description, str(object.status),
                        object.priority, str(object.kind), object.end_date,
                        object.creation_date, object.project_id,)
                    )
        except psycopg2.ProgrammingError as error:
            print(error)
        finally:
            conn.close()

    def update(self, object) -> None:

        query = """
                UPDATE tasks
                SET name=?, description=?, status=?, priority=?, kind=?,
                    start_date=?, end_date=?, project_id=?
                WHERE id=?
                """

        config = load_config()
        
        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query,
                        (object.name, object.description, object.status, object.priority,
                        object.kind, object.start_date, object.end_date,
                        object.project_id if object.project_id else None, object.id,)
                    )
                conn.commit()
        except psycopg2.ProgrammingError as error:
            # raise (f"There was a problem trying to ADD the project with the id {object.id}")
            print(error)
        finally:
            conn.close()

    def delete(self, object_id: str) -> None:

        query = "DELETE FROM tasks WHERE id=?"

        config = load_config()

        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (str(object_id),))
        except psycopg2.ProgrammingError as error:
            print(error)
        finally:
            conn.close()

    def row_to_object(self, row) -> Task:
        return Task(
            name=row["name"],
            end_date=row["end_date"],
            priority=row["priority"],
            kind=row["kind"],
            status=row["status"],
            description=row["description"],
            project_id=row["project_id"],
        )