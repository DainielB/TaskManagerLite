from PySide6.QtCore import QDate

from .entity import Entity
from constants import (
    TaskStatus,
    TaskPriority,
    TaskKind,
    TaskPriorityColor,
    DATE_FORMAT,
)


class Task(Entity):

    # def __init__(self, name: str, end_date: str, priority: str, kind: str, status: str, description: str, project_id: str) -> None:
    def __init__(self, name: str, end_date: str, priority: int, kind: str, status: str, description: str, project_id: str) -> None:
        super().__init__(name, QDate.fromString(end_date, DATE_FORMAT), description)

        # self._priority: str = priority if priority != "Priority" else TaskPriority.Low.name
        self._priority: int = priority if priority else TaskPriority.Low.value
        self._kind: str = kind

        self._status: str = status
        if status in (None, "Initial Status"):
            self._status= TaskStatus.TO_DO.value

        self._color: str = TaskPriorityColor[self.priority.name].value

        self._project_id: str = None
        if project_id:
            self._project_id: str = str(project_id)

    def __str__(self) -> str:
        return f"TASK\r\n id: {self.id}, name: {self.name}, end_date: {self.end_date}, priority: {self.priority}, kind: {self.kind}, status: {self.status}, description: {self.description}\n, project_id: {self.project_id}"

    @property
    def priority(self) -> TaskPriority:
        return TaskPriority(self._priority)

    @priority.setter
    def priority(self, priority: TaskPriority) -> None:
        self._priority = priority.value

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
            new_start_date = QDate.currentDate()
            self.start_date = new_start_date

        self._status = new_status.value

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, new_color: str) -> None:
        self._color = new_color

    @property
    def project_id(self) -> str:
        return self._project_id