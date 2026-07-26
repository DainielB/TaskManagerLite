from datetime import date
from enum import IntEnum, auto

from PySide6.QtCore import (
    Qt,
    QAbstractListModel,
    QModelIndex,
    QPersistentModelIndex,
    Slot,
)


class TaskItemRoles(IntEnum):
    ID = Qt.ItemDataRole.UserRole + 1
    START_DATE = auto()
    END_DATE = auto()
    STATUS = auto()
    DESCRIPTION = auto()
    NAME = auto()
    TYPE = auto()
    PRIORITY = auto()
    PROJECT = auto()
    CREATION_DATE = auto()
    # COLOR = auto()


_role_names = {
    TaskItemRoles.ID: b'id',
    TaskItemRoles.START_DATE: b'start_date',
    TaskItemRoles.END_DATE: b'end_date',
    TaskItemRoles.STATUS: b'status',
    TaskItemRoles.DESCRIPTION: b'description',
    TaskItemRoles.NAME: b'name',
    TaskItemRoles.TYPE: b'type',
    TaskItemRoles.PRIORITY: b'priority',
    TaskItemRoles.PROJECT: b'project',
    TaskItemRoles.CREATION_DATE: b'creation_date',
    # TaskItemRoles.COLOR: b'color',
}


class TaskTableModel(QAbstractListModel):

    def __init__(self):
        super().__init__()
        self._tasks: list = []

        self.add_task("Project Task 1", "2025-01-01", "In Progress", "High", "Project 1")
        self.add_task("Project Task 2", "2025-01-01", "In Progress", "Low", "Project 1")
        self.add_task("Project Task 3", "2025-01-01", "In Progress", "Medium", "Project 1")

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

        if role not in list(_role_names):
            return None

        try:
            task = self._tasks[index.row()]
        except IndexError:
            return None

        if role in task:
            return task[role]

        return None

    def roleNames(self) -> dict:
        return _role_names

    @Slot(str)
    def add_task(self, name: str, end_date: date, type: str, status: str = "", priority: str = "", description: str = "") -> None:
        """Adds a task to the task list at the specified index with the given name."""

        if len(self._tasks) == 0:
            new_index = 0
        else:
            new_index = len(self._tasks)

        new_task = { TaskItemRoles.NAME: name, TaskItemRoles.END_DATE: end_date, TaskItemRoles.TYPE: type, TaskItemRoles.STATUS: status, TaskItemRoles.PRIORITY: priority, TaskItemRoles.DESCRIPTION: description }

        self.beginInsertRows(QModelIndex(), new_index, new_index)
        self._tasks.insert(new_index, new_task)
        self.endInsertRows()
