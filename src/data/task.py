from uuid import UUID

from PySide6.QtCore import QDate

from .entity import Entity
from constants import (
    TaskStatus,
    TaskPriority,
    TaskKind,
    DATE_FORMAT,
)


class Task(Entity):

    def __init__(self, name: str, end_date: str, priority: str, kind: str, status: str, description: str, project_id: str) -> None:
        super().__init__(name, QDate.fromString(end_date, DATE_FORMAT), description)

        self._priority: str = priority if priority != "Priority" else TaskPriority.Low.name
        self._kind: str = kind
        # self._status: str = status if status not in (None , "Initial Status") else TaskStatus.TO_DO.value

        if status in (None, "Initial Status"):
            self._status = TaskStatus.TO_DO.value
        else:
            self._status = status


        if project_id:
            self._project_id: str = str(project_id)
        else:
            self._project_id: str = None

    def __str__(self) -> str:
        return f"TASK\r\n id: {self.id}, name: {self.name}, end_date: {self.end_date.toString(DATE_FORMAT)}, priority: {self.priority}, kind: {self.kind}, status: {self.status}, description: {self.description}\n, project_id: {self.project_id}"

    @property
    def priority(self) -> str:
        return self._priority

    @priority.setter
    def priority(self, priority: TaskPriority) -> None:
        self._priority = priority.name

    @property
    def kind(self) -> str:
        return self._kind

    @kind.setter
    def kind(self, kind: TaskKind) -> None:
        self._kind = kind.value

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, new_status: TaskStatus) -> None:
        if new_status == TaskStatus.IN_PROGRESS and self.status != TaskStatus.IN_PROGRESS:
            self.start_date = QDate.currentDate()

        self._status = new_status.value

    @property
    def project_id(self) -> str:
        return self._project_id
