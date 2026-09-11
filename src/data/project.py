from PySide6.QtCore import QDate

from .entity import Entity
from constants import ProjectStatus, DATE_FORMAT


class Project(Entity):

    def __init__(self, name: str, end_date: str, description: str, id: str = None) -> None:
        super().__init__(name, QDate.fromString(end_date, DATE_FORMAT), description, id)

        self._status: str = ProjectStatus.READY_TO_START.value

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, end_date: {self._end_date}, description: {self.description}"

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, new_status: ProjectStatus) -> None:
        if new_status == ProjectStatus.IN_PROGRESS and self.status != ProjectStatus.IN_PROGRESS:
            self.start_date = QDate.currentDate()

        self._status = new_status
