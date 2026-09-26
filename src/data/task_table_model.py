from typing import Any

from PySide6.QtCore import (
    QAbstractListModel,
    QModelIndex,
    QPersistentModelIndex,
    Slot,
)

from constants import (
    TaskRoles,
    task_role_names,
    DATE_FORMAT
)
from src.data.task import Task
from src.data.task_repository import TaskRepository


class TaskTableModel(QAbstractListModel):

    def __init__(self):
        super().__init__()

        self._repository: TaskRepository = TaskRepository()
        self._tasks: list[Task] = []

    @property
    def repository(self) -> TaskRepository:
        return self._repository

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        Returns the number of rows under the given parent.
        When the parent is valid it means that rowCount is returning
        the number of children of parent.
        """

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

        if role not in task_role_names:
            return None

        task = self._tasks[index.row()]

        if role == TaskRoles.ID:
            return task.id
        elif role == TaskRoles.START_DATE:
            return task.start_date
        elif role == TaskRoles.END_DATE:
            return task.end_date
        elif role == TaskRoles.STATUS:
            return task.status
        elif role == TaskRoles.DESCRIPTION:
            return task.description
        elif role == TaskRoles.NAME:
            return task.name
        elif role == TaskRoles.KIND:
            return task.kind
        elif role == TaskRoles.PRIORITY:
            return task.priority.value
        elif role == TaskRoles.PRIORITY_LABEL:
            return task.priority.name
        elif role == TaskRoles.COLOR:
            return task.color
        elif role == TaskRoles.CREATION_DATE:
            return task.creation_date
        elif role == TaskRoles.TASK:
            return task

        return None

    def roleNames(self) -> dict:
        return task_role_names

    def setData(self, index: QModelIndex, value: Any, role: int) -> bool:
        if not index.isValid():
            return False

        task = self._tasks[index.row()]
        self._repository.update(task)

        self.dataChanged.emit(index, index, list(self.roleNames().keys()))

        return super().setData(index, value, role)

    @Slot(Task)
    def add_task(self, task: Task, insert: bool = False) -> None:
        """Adds a task to the task list at the specified index with the given name.

        Args:
            task (Task): Task object to add to the model
            insert (bool, optional): If true the task will be inserted in the database. Defaults to False.
        """

        new_index = len(self._tasks)

        if len(self._tasks) == 0:
            new_index = 0

        self.beginInsertRows(QModelIndex(), new_index, new_index)
        self._tasks.append(task)
        self.endInsertRows()

        if insert:
            self._repository.add(task)

    @Slot(str)
    def remove_task(self, task_id: str) -> None:

        for row, task in enumerate(self._tasks):
            if task.id != task_id:
                continue           

            '''
            if not (0 <= row < len(self._tasks)):
                return
            '''

            self.beginRemoveRows(QModelIndex(), row, row)
            task = self._tasks.pop(row)
            self._repository.delete_task(task_id)
            self.endRemoveRows()
            return

    def get_task_by_id(self, task_id: id) -> Task:
        for task in self._tasks:
            if task_id == task.id:
                return task

        return None

    def get_index_task(self, task_id: str) -> QModelIndex:

        row_count: int = self.rowCount()

        for row in range(row_count):
            index = self.index(row, 0)
            if self.data(index, TaskRoles.ID) == task_id:
                return index

        return QModelIndex()

    @Slot(str)
    def refresh_table(self, project_id: str = None) -> None:
        """Refresh the table UI.

        Args:
            project_id (str, optional): Id of the project to get the tasks from. Defaults to None.
        """

        self.beginResetModel()
        self._tasks = self._repository.get_all(project_id)
        self.endResetModel()