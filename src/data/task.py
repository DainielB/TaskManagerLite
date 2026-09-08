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

        if isinstance(priority, TaskPriority):
            self._priority = priority
        elif priority in (None, "Priority"):
            self._priority = TaskPriority.Low
        elif isinstance(priority, str) and priority.startswith("TaskPriority."):
            self._priority = TaskPriority[priority.split(".", 1)[1]]
        elif isinstance(priority, str) and priority.isdigit():
            self._priority = TaskPriority(int(priority))
        else:
            self._priority = TaskPriority[priority]

        if isinstance(kind, TaskKind):
            self._kind = kind
        elif isinstance(kind, str) and kind.startswith("TaskKind."):
            self._kind = TaskKind[kind.split(".", 1)[1]]
        else:
            self._kind = TaskKind(kind)

        if isinstance(status, TaskStatus):
            self._status = status
        elif status in (None, "Initial Status"):
            self._status = TaskStatus.TO_DO
        elif isinstance(status, str) and status.startswith("TaskStatus."):
            self._status = TaskStatus[status.split(".", 1)[1]]
        else:
            self._status = TaskStatus(status)

        self._project_id: UUID = project_id

    def __str__(self) -> str:
        return f"TASK\r\n id: {self.id}, name: {self.name}, end_date: {self.end_date}, start_date: {self.start_date}, priority: {self.priority}, kind: {self.kind}, status: {self.status}, description: {self.description}\n "

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
