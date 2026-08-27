from uuid import UUID

from PySide6.QtCore import(
    Property,
    QObject,
    Signal,
    Slot,
)

from constants import TaskRoles, TaskStatus
from src.data.task import Task
from src.data.task_filter_proxy import TaskFilterProxy


class TaskTableController(QObject):

    taskClicked = Signal(Task)

    def __init__(self, model, parent=None):
        super().__init__(parent)

        self._model = model

        '''
        self._in_progress_proxy = TaskFilterProxy(TaskStatus.IN_PROGRESS, self._model)
        self._in_progress_proxy.setFilterKeyColumn(0)
        self._in_progress_proxy.setDynamicSortFilter(True)
        self._in_progress_proxy.setFilterRole(TaskRoles.STATUS)
        self._in_progress_proxy.setSortRole(TaskRoles.STATUS)

        self._in_review_proxy = TaskFilterProxy(TaskStatus.IN_REVIEW, self._model)
        self._in_review_proxy.setFilterKeyColumn(0)
        self._in_review_proxy.setDynamicSortFilter(True)
        self._in_review_proxy.setFilterRole(TaskRoles.STATUS)
        self._in_review_proxy.setSortRole(TaskRoles.STATUS)

        self._to_do_proxy = TaskFilterProxy(TaskStatus.TO_DO, self._model)
        self._to_do_proxy.setFilterKeyColumn(0)
        self._to_do_proxy.setDynamicSortFilter(True)
        self._to_do_proxy.setFilterRole(TaskRoles.STATUS)
        self._to_do_proxy.setSortRole(TaskRoles.STATUS)

        self._paused_proxy = TaskFilterProxy(TaskStatus.PAUSED, self._model)
        self._paused_proxy.setFilterKeyColumn(0)
        self._paused_proxy.setDynamicSortFilter(True)
        self._paused_proxy.setFilterRole(TaskRoles.STATUS)
        self._paused_proxy.setSortRole(TaskRoles.STATUS)

        self._backlog_proxy = TaskFilterProxy(TaskStatus.BACKLOG, self._model)
        self._backlog_proxy.setFilterKeyColumn(0)
        self._backlog_proxy.setDynamicSortFilter(True)
        self._backlog_proxy.setFilterRole(TaskRoles.STATUS)
        self._backlog_proxy.setSortRole(TaskRoles.STATUS)

        self._finished_proxy = TaskFilterProxy(TaskStatus.FINISHED, self._model)
        self._finished_proxy.setFilterKeyColumn(0)
        self._finished_proxy.setDynamicSortFilter(True)
        self._finished_proxy.setFilterRole(TaskRoles.STATUS)
        self._finished_proxy.setSortRole(TaskRoles.STATUS)
        '''

        self._selected_task_id: UUID = None

        # self.taskClicked.connect(self.get_task_by_id)

    @Property(QObject, constant=True)
    def task_table_model(self):
        return self._model

    '''
    @Property(QObject, constant=True)
    def task_filter_proxy(self):
        return self._task_filter_proxy
    '''

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
    '''

    @property
    def selected_task_id(self) -> UUID:
        return self._selected_task_id

    @selected_task_id.setter
    def selected_task_id(self, id: UUID) -> None:
        self._selected_task_id = id

    @Slot(str, str, str, str, str, str)
    def add_new_task(self, name: str, end_date: str, priority: str, kind: str, status: str = "", description: str = "") -> None:
        """
        Adds a task to the task table with the given info.
        """
        new_task = Task(name, end_date, priority, kind, status, description)

        self._model.add_task(new_task)
