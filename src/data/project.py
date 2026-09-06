# from dataclasses import dataclass

from PySide6.QtCore import QDate

from .entity import Entity
from constants import DATE_FORMAT


# @dataclass
class Project(Entity):

    def __init__(self, name: str, end_date: str, description: str) -> None:
        super().__init__(name, QDate.fromString(end_date, DATE_FORMAT), description)

        # self._start_date: QDate # Sets when Project status is created
        # self._end_date: QDate = QDate.fromString(end_date, Qt.DateFormat.ISODate)
        # self._description: str = description
        # self._creation_date: QDate = QDate.currentDate()

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, description: {self.description}, end_date: {self.end_date}"
