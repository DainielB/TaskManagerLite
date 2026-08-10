from PySide6.QtCore import(
    Property,
    QDate,
    QObject,
    Slot,
    Qt
)

from constants import TaskStatus
from src.data.task_table_model import TaskTableModel
from src.data.task import Task
from src.data.task_filter_proxy import TaskFilterProxy


class TaskTableController(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._task_table_model = TaskTableModel()

        self._in_progress_proxy = TaskFilterProxy(TaskStatus.IN_PROGRESS, self._task_table_model)
        self._in_review_proxy = TaskFilterProxy(TaskStatus.IN_REVIEW, self._task_table_model)
        self._to_do_proxy = TaskFilterProxy(TaskStatus.TO_DO, self._task_table_model)
        self._paused_proxy = TaskFilterProxy(TaskStatus.PAUSED, self._task_table_model)
        self._backlog_proxy = TaskFilterProxy(TaskStatus.BACKLOG, self._task_table_model)
        self._finished_proxy = TaskFilterProxy(TaskStatus.FINISHED, self._task_table_model)

    @Property(QObject, constant=True)
    def task_table_model(self):
        return self._task_table_model

    '''
    @Property(QObject, constant=True)
    def task_filter_proxy(self):
        return self._task_filter_proxy
    '''

    @Property(QObject, constant=True)
    def in_progress_proxy(self):
        return self._in_progress_proxy

    @Property(QObject, constant=True)
    def in_review_proxy(self):
        return self._in_review_proxy

    @Property(QObject, constant=True)
    def to_do_proxy(self):
        return self._to_do_proxy

    @Property(QObject, constant=True)
    def paused_proxy(self):
        return self._paused_proxy

    @Property(QObject, constant=True)
    def backlog_proxy(self):
        return self._backlog_proxy

    @Property(QObject, constant=True)
    def finished_proxy(self):
        return self._finished_proxy

    @Slot(str, str, str, str, str, str)
    def add_new_task(self, name: str, end_date: str, priority: str, kind: str, status: str = "", description: str = "") -> None:
        """
        Adds a task to the task table with the given info.
        """
        new_task = Task(name, end_date, priority, kind, status, description)

        self._task_table_model.add_task(new_task)
