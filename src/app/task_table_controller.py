from PySide6.QtCore import Property, QObject, Slot

from src.data.task_table_model import TaskTableModel
from src.data.task import Task


class TaskTableController(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._task_table_model = TaskTableModel()

    @Property(QObject, constant=True)
    def task_table_model(self):
        return self._task_table_model

    @Slot(str, str, str, str)
    def add_new_project(self, name: str, description: str, limit_date: str, color: str) -> None:
        """
        Adds a project to the project list at the specified index with the given info.
        """

        new_task = Task(name, description, limit_date, color)

        self._task_table_model.add_task(new_task.name, new_task.description, new_task.end_date, new_task.color)
