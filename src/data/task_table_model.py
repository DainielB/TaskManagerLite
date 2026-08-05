from datetime import date

from PySide6.QtCore import (
    Qt,
    QAbstractListModel,
    QModelIndex,
    QPersistentModelIndex,
    Slot,
    QDate,
    QDateTime
)

from constants import TaskItemRoles, role_names


class TaskTableModel(QAbstractListModel):

    def __init__(self):
        super().__init__()
        self._tasks: list = []

        self.add_task("Broject Task 1", "2025-01-01", "High", "Modeling", "In Progress", "Project 1")
        self.add_task("Aroject Task 2", "2025-01-01", "Low", "Lighting", "To Do", "Project 1")
        self.add_task("Project Task 3", "2025-01-01", "Medium", "FX", "Backlog", "Project 1")

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

    @Slot(str)
    def add_task(self, name: str, end_date: QDate, priority: str = "", type: str = "", status: str = "", description: str = "") -> None:
        """Adds a task to the task list at the specified index with the given name."""

        if len(self._tasks) == 0:
            new_index = 0
        else:
            new_index = len(self._tasks)

        new_task = { TaskItemRoles.NAME: name, TaskItemRoles.END_DATE: end_date, TaskItemRoles.PRIORITY: priority, TaskItemRoles.TYPE: type, TaskItemRoles.STATUS: status, TaskItemRoles.DESCRIPTION: description }

        self.beginInsertRows(QModelIndex(), new_index, new_index)
        self._tasks.insert(new_index, new_task)
        self.endInsertRows()
