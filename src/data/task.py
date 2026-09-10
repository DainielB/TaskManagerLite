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

    def __init__(self, name: str, end_date: str, priority: str, kind: str, status: str, description: str, project_id: UUID) -> None:
        super().__init__(name, QDate.fromString(end_date, DATE_FORMAT), description)

        self._priority = priority
        self._kind = kind

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
    def priority(self) -> TaskPriority:
        return self._priority

    @priority.setter
    def priority(self, priority: TaskPriority) -> None:
        self._priority = priority

    @property
    def kind(self) -> TaskKind:
        return self._kind

    @kind.setter
    def kind(self, kind: TaskKind) -> None:
        self._kind = kind

    @property
    def project_id(self) -> UUID:
        return self._project_id
