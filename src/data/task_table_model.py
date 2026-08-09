from datetime import date

from PySide6.QtCore import (
    Qt,
    QAbstractListModel,
    QModelIndex,
    QPersistentModelIndex,
    Slot,
    QDate,
)

from constants import TaskItemRoles, role_names
from src.app.task_table_controller import TaskPriority, TaskStatus, TaskKind
from src.data.task import Task


class TaskTableModel(QAbstractListModel):

    def __init__(self):
        super().__init__()
        self._tasks: list = []

        task_one = Task("Project Task 1", "2025-08-09", TaskPriority.HIGH, TaskKind.LIGHTING, TaskStatus.IN_PROGRESS, "Project 1")
        self.add_task(task_one)
        task_two = Task("Aroject Task 2", "2026-01-01", TaskPriority.LOW, TaskKind.ANIMATION, TaskStatus.TO_DO, "Project 1")
        self.add_task(task_two)
        task_three = Task("Project Task 3", "2025-06-01", TaskPriority.MEDIUM, TaskKind.FX, TaskStatus.BACKLOG, "Project 1")
        self.add_task(task_three)

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        Returns the number of rows under the given parent.
        When the parent is valid it means that rowCount is returning
        the number of children of parent.
        """

        if parent.isValid():
            return 0

        return len(self._tasks)

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = Qt.DisplayRole):
        """Returns an appropriate value for the requested data.
        If the view requests an invalid index, an invalid variant is returned.
        Any valid index that corresponds to a string in the list causes that
        string to be returned."""

        if role not in list(role_names):
            return None

        try:
            task = self._tasks[index.row()]
        except IndexError:
            return None

        if role in task:
            return task[role]

        return None

    def roleNames(self) -> dict:
        return role_names

    '''
    @Slot(str, str, str, str, str, str)
    def add_task(self, name: str, end_date: str, priority: str, kind: str, status: str = "", description: str = "") -> None:
        """Adds a task to the task list at the specified index with the given name."""

        if len(self._tasks) == 0:
            new_index = 0
        else:
            new_index = len(self._tasks)

        new_task = { TaskItemRoles.NAME: name, TaskItemRoles.END_DATE: end_date.toString(Qt.DateFormat.ISODate), TaskItemRoles.PRIORITY: priority, TaskItemRoles.KIND: kind, TaskItemRoles.STATUS: status, TaskItemRoles.DESCRIPTION: description }

        self.beginInsertRows(QModelIndex(), new_index, new_index)
        self._tasks.insert(new_index, new_task)
        self.endInsertRows()
    '''

    @Slot(Task)
    def add_task(self, task: Task) -> None:
        """Adds a task to the task list at the specified index with the given name."""

        if len(self._tasks) == 0:
            new_index = 0
        else:
            new_index = len(self._tasks)

        new_task = { TaskItemRoles.NAME: task.name, TaskItemRoles.END_DATE: task.end_date.toString(Qt.DateFormat.ISODate), TaskItemRoles.PRIORITY: task.priority.value, TaskItemRoles.KIND: task.kind.value, TaskItemRoles.STATUS: task.status, TaskItemRoles.DESCRIPTION: task.description }

        self.beginInsertRows(QModelIndex(), new_index, new_index)
        self._tasks.insert(new_index, new_task)
        self.endInsertRows()
