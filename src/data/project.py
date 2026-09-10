from PySide6.QtCore import QDate

from .entity import Entity
from constants import ProjectStatus, DATE_FORMAT


class Project(Entity):

    def __init__(self, name: str, end_date: str, description: str) -> None:
        super().__init__(name, QDate.fromString(end_date, DATE_FORMAT), description)

        self._status: str = ProjectStatus.READY_TO_START.value
        # self._start_date: QDate # Sets when Project status is created
        # self._end_date: QDate = QDate.fromString(end_date, Qt.DateFormat.ISODate)
        # self._description: str = description
        # self._creation_date: QDate = QDate.currentDate()

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, status: {self._status}, description: {self.description}, end_date: {self.end_date}"
