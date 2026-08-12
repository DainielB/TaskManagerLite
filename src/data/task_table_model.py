from uuid import UUID
from PySide6.QtCore import (
    Qt,
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

        if parent.isValid():
            return 0

        return len(self._tasks)

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = Qt.DisplayRole) -> Task:
        """
        Returns an appropriate value for the requested data.
        If the view requests an invalid index, an invalid variant is returned.
        Any valid index that corresponds to a string in the list causes that
        string to be returned.
        """

        if role not in list(role_names):
            return None

        task = self._tasks[index.row()]

        '''
        if role == TaskRoles.ID:
            return task.id
        elif role == TaskRoles.START_DATE:
            return task.start_date.toString(DATE_FORMAT)
        elif role == TaskRoles.END_DATE:
            return task.end_date.toString(DATE_FORMAT)
        elif role == TaskRoles.STATUS:
            return str(task.status)
        elif role == TaskRoles.DESCRIPTION:
            return task.description
        elif role == TaskRoles.NAME:
            return task.name
        elif role == TaskRoles.KIND:
            return str(task.kind)
        elif role == TaskRoles.PRIORITY:
            return str(task.priority)
        elif role == TaskRoles.CREATION_DATE:
            return task.creation_date.toString(DATE_FORMAT)
        '''

        try:
            task = self._tasks[index.row()]
        except IndexError:
            return None # Set an error message

        if role in task:
            return task[role]

        return None

    def roleNames(self) -> dict:
        return role_names

    @Slot(Task)
    def add_task(self, task: Task) -> None:
        """Adds a task to the task list at the specified index with the given name."""

        if len(self._tasks) == 0:
            new_index = 0
        else:
            new_index = len(self._tasks)

        new_task = { TaskRoles.ID: task.id, TaskRoles.NAME: task.name, TaskRoles.END_DATE: task.end_date.toString(Qt.DateFormat.ISODate), TaskRoles.PRIORITY: task.priority.value, TaskRoles.KIND: task.kind.value, TaskRoles.STATUS: task.status, TaskRoles.DESCRIPTION: task.description }

        self.beginInsertRows(QModelIndex(), new_index, new_index)
        self._tasks.insert(new_index, new_task)
        self.endInsertRows()

    @Slot(UUID)
    def get_task_by_id(self, id: UUID) -> Task:
        # print(f"ID type: {type(id)}")

        # task_id = uuid.UUID(id)

        for task in self._tasks:
            if id == task[TaskRoles.ID]:
                return task

        return None
