from dataclasses import dataclass

from PySide6.QtCore import QDate, Qt

from .entity import Entity
from constants import TaskStatus, TaskPriority, TaskKind


# @dataclass
class Task(Entity):

    def __init__(self, name: str, end_date: str, priority: str, kind: str, status: str, description: str = "") -> None:
        super().__init__()

        self._id: str
        self._name: str = name
        self._start_date: QDate # Sets when Task status is TaskStatus.IN_PROGRESS
        self._end_date: QDate = QDate.fromString(end_date, Qt.DateFormat.ISODate)
        self._priority: TaskPriority = TaskPriority(priority) if priority != "Priority" else TaskPriority.LOW
        self._kind: TaskKind = TaskKind(kind)
        self._status: TaskStatus = TaskStatus(status) if status != "Initial Status" else TaskStatus.TO_DO

        self._description: str = ""
        self._creation_date: QDate = QDate.currentDate()
        # self.color: str = color

    def __str__(self) -> str:
        return f"TASK\r\n name: {self.name}, end_date: {self.end_date}, priority: {self.priority}, kind: {self.kind}, status: {self.status}, description: {self.description}, "

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
