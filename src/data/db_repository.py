from abc import abstractmethod
import sqlite3
from uuid import UUID

from PySide6.QtCore import QObject

from constants import DB_PATH


class DB_Repository:

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
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
    def row_to(self, row: sqlite3.Row) -> QObject: ...
