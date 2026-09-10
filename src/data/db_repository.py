from abc import ABC, abstractmethod
from sqlite3 import Connection, Row, connect
from uuid import UUID

from PySide6.QtCore import QObject

from constants import DB_PATH


class DB_Repository(ABC):

    def _connect(self) -> Connection:
        conn = connect(DB_PATH)
        conn.row_factory = Row
        return conn

    @abstractmethod
    def get_all(self) -> list[QObject]: ...

    @abstractmethod
    def add(self, object: QObject) -> None: ...

    @abstractmethod
    def delete(self, object_id: UUID) -> None: ...

    @abstractmethod
    def update(self, object: QObject) -> None: ...

    @abstractmethod
    def row_to_object(self, row: Row) -> QObject: ...
