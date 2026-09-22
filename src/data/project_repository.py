import psycopg2
from psycopg2.extras import DictCursor

from src.data.db_repository import DB_Repository
from src.data.project import Project
from constants import DATE_FORMAT
from config import load_config


class ProjectRepository(DB_Repository):

    def get_all(self, object_id: str = None) -> list[Project]:

        query = "SELECT * FROM projects"

        config = load_config()

        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor(ursor_factory=psycopg2.extras.DictCursor) as cursor:

                    """
                    if object_id:
                        query = "SELECT * FROM tasks WHERE project_id=?"
                        cursor.execute(query, (object_id,))
                    else:
                        query = "SELECT * FROM projects"
                        cursor.execute(query)
                    """

                    cursor.execute(query)
                    rows = cursor.fetchmany()
        
                    return [self.row_to_object(row) for row in rows]
        except psycopg2.ProgrammingError as error:
            # raise ("There was a problem trying to get all projects")
            print(error)
        finally:
            conn.close()
            return []

    def add(self, object: Project) -> None:

        query = """INSERT INTO projects (id, name, description, end_date, creation_date)
                VALUES (%s, %s, %s, %s, %s)
                """

        config = load_config()
        conn = psycopg2.connect(**config)
        
        try:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query,
                    (str(object.id), object.name, object.description, object.end_date, object.creation_date)
                )
                # conn.commit()

                # May be raise an exception if there's nothing in the database???
        except psycopg2.ProgrammingError as error:
            # raise (f"There was a problem trying to ADD the project with the id {object.id}")
            print(error)
        finally:
            conn.close()

    def update(self, object: Project) -> None:

        query = """ 
                UPDATE projects
                SET name=%s, description=%s, start_date=%s, end_date=%s
                WHERE id=%s
                """

        config = load_config()

        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                    cursor.execute(query,
                        (object.name, object.description, object.start_date, object.end_date, object.id)
                    )
                    #conn.commit()
        except psycopg2.ProgrammingError as error:
            # raise (f"There was a problem trying to UPDATE the project with the id {object.id}")
            print(error)
        finally:
            conn.close()

    def delete(self, object_id: str) -> None:

        query = "DELETE FROM projects WHERE id=?"

        config = load_config()

        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (object_id,))
                    # conn.commit()
        except psycopg2.ProgrammingError as error:
            # raise (f"There was a problem trying to UPDATE the project with the id {object.id}")
            print(error)
        finally:
            conn.close()

    def row_to_object(self, row) -> Project:
        return Project (
            name=row["name"],
            end_date=row["end_date"],
            description=row["description"],
            id=row["id"]
        )

    def delete_tasks_by_project_id(self, project_id: str) -> None:

        query = "DELETE FROM tasks WHERE project_id=?"

        config = load_config()

        try:
            with psycopg2.connect(**config) as conn:
                conn.execute(query, (project_id,))
                # conn.commit()
        except psycopg2.ProgrammingError as error:
            print(error)
        finally:
            conn.close()