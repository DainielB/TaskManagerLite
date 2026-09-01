from typing import Any
from uuid import UUID

from PySide6.QtCore import (
    QAbstractListModel,
    QModelIndex,
    QPersistentModelIndex,
    Slot,
)

from constants import (
    TaskRoles,
    role_names,
    TaskPriority,
    TaskStatus,
    TaskKind,
    DATE_FORMAT
)
from src.data.task import Task


class TaskTableModel(QAbstractListModel):

    def __init__(self):
        super().__init__()
        self._tasks: list = []

        task_one = Task("Project Task 1", "2025-09-08", TaskPriority.HIGH, TaskKind.LIGHTING, TaskStatus.IN_PROGRESS, "Project 1")
        self.add_task(task_one)
        task_two = Task("Aroject Task 2", "2026-01-01", TaskPriority.LOW, TaskKind.ANIMATION, TaskStatus.TO_DO, "Project 1")
        self.add_task(task_two)
        task_three = Task("Project Task 3", "2025-12-01", TaskPriority.MEDIUM, TaskKind.FX, TaskStatus.BACKLOG, "Project 1")
        self.add_task(task_three)
        task_four = Task("Project Task 4", "2025-12-01", TaskPriority.URGENT, TaskKind.MODELING, TaskStatus.IN_PROGRESS, "Project 1")
        self.add_task(task_four)

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        Returns the number of rows under the given parent.
        When the parent is valid it means that rowCount is returning
        the number of children of parent.
        """

        '''
        if parent.isValid():
            return 0
        '''

        return len(self._tasks)

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex) -> int:
        return 1

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int):
        """
        Returns an appropriate value for the requested data.
        If the view requests an invalid index, an invalid variant is returned.
        Any valid index that corresponds to a string in the list causes that
        string to be returned.
        """

        if not index.isValid() or not (0 <= index.row() < len(self._tasks)):
            return None

        if role not in role_names:
            return None

        task = self._tasks[index.row()]

        if role == TaskRoles.ID:
            return task.id
        elif role == TaskRoles.START_DATE:
            return task.start_date.toString(DATE_FORMAT)
        elif role == TaskRoles.END_DATE:
            return task.end_date.toString(DATE_FORMAT)
        elif role == TaskRoles.STATUS:
            return task.status.value
        elif role == TaskRoles.DESCRIPTION:
            return task.description
        elif role == TaskRoles.NAME:
            return task.name
        elif role == TaskRoles.KIND:
            return task.kind.value
        elif role == TaskRoles.PRIORITY:
            return task.priority.value
        elif role == TaskRoles.CREATION_DATE:
            return task.creation_date.toString(DATE_FORMAT)
        elif role == TaskRoles.TASK:
            return task

        return None

    def roleNames(self) -> dict:
        return role_names

    def setData(self, index: QModelIndex, value: Any, role: int) -> bool:

        self.dataChanged.emit(index, index, list(self.roleNames().keys())) # or self.roleNames().keys()

        return super().setData(index, value, role)

    @Slot(Task)
    def add_task(self, task: Task) -> None:
        """Adds a task to the task list at the specified index with the given name."""

        new_index = len(self._tasks)

        if len(self._tasks) == 0:
            new_index = 0

        self.beginInsertRows(QModelIndex(), new_index, new_index)
        self._tasks.append(task)
        self.endInsertRows()

    @Slot(UUID)
    def get_task_by_id(self, task_id: UUID) -> Task:
        for task in self._tasks:
            if str(task_id) == str(task.id):
                return task

        return None

    def get_index_task(self, task_id: UUID) -> QModelIndex:

        row_count: int = self.rowCount()

        for row in range(row_count):
            index = self.index(row, 0)
            if self.data(index, TaskRoles.ID) == task_id:
                return index

        return QModelIndex()
