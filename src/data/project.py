from dataclasses import dataclass

from PySide6.QtCore import QDate, Qt

from .entity import Entity


@dataclass
class Project(Entity):

    def __init__(self, name: str, description: str, end_date: str, color: str) -> None:
        super().__init__()

        self._id: str
        self._name: str = name
        self._start_date: QDate # Sets when Project status is created
        self._end_date: QDate = QDate.fromString(end_date, Qt.DateFormat.ISODate)
        # self._status: str
        self._description: str = description
        self._creation_date: QDate
        # self.color: str = color

    def __str__(self) -> str:
        return f"name: {self.name}, description: {self.description}, end_date: {self.end_date}, color: {self.color}"
