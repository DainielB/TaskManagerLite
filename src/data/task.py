from PySide6.QtCore import QDate

from .entity import Entity
from constants import (
    TaskStatus,
    TaskPriority,
    TaskKind,
    DATE_FORMAT,
)


class Task(Entity):

    def __init__(self, name: str, end_date: str, priority: str, kind: str, status: str, description: str) -> None:
        super().__init__(name, QDate.fromString(end_date, DATE_FORMAT), description)

        self._priority: TaskPriority = TaskPriority(priority) if priority != "Priority" else TaskPriority.Low
        self._kind: TaskKind = TaskKind(kind)
        self._status: TaskStatus = TaskStatus(status) if status != "Initial Status" else TaskStatus.TO_DO
        # self.color: str = color

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
