from abc import ABC, abstractmethod

import psycopg2
from PySide6.QtCore import QObject

from config import load_config


class DB_Repository(ABC):

    def connect(self, config):
        """ Connect to the PostgreSQL database server """
        try:
            # connecting to the PostgreSQL server
            with psycopg2.connect(**config) as conn:
                print('Connected to the PostgreSQL server.')
                return conn
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    @abstractmethod
    def get_all(self) -> list[QObject]: ...

    @abstractmethod
    def add(self, object: QObject) -> None: ...

    @abstractmethod
    def delete(self, object_id: str) -> None: ...

    @abstractmethod
    def update(self, object: QObject) -> None: ...

    @abstractmethod
    def row_to_object(self, row) -> QObject: ...
