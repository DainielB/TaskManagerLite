from datetime import date

from PySide6.QtCore import Property, QObject, Slot

from src.data.task_table_model import TaskTableModel
from src.data.task import Task
from src.data.task_filter_proxy import TaskFilterProxy


class TaskTableController(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._task_table_model = TaskTableModel()
        # self._task_filter_proxy = TaskFilterProxy(status="In Progress", source_model=
        self._task_filter_proxy = TaskFilterProxy(self._task_table_model)

    @Property(QObject, constant=True)
    def task_table_model(self):
        return self._task_table_model

    @Property(QObject, constant=True)
    def task_filter_proxy(self):
        return self._task_filter_proxy

    @Slot(str, str, str, str, str, str)
    def add_new_task(self, name: str, end_date: date, type: str, status: str = "", priority: str = "", description: str = "") -> None:
        """
        Adds a task to the task table with the given info.
        """

        new_task = Task(name, end_date, type)

        self._task_table_model.add_task(new_task.name, new_task.end_date, new_task.type, new_task.status, new_task.priority, new_task.description)
