from PySide6.QtCore import QObject, Property

from src.data.task_sort_filter_proxy import TaskSortFilterProxy
from src.data.task_table_model import TaskTableModel
from src.data.database import init_db

from src.app.project_list_controller import ProjectListController
from src.app.task_table_controller import TaskTableController
from src.app.task_info_controller import TaskInfoController


class AppController(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)

        init_db()

        self._task_table_model = TaskTableModel()

        self._project_list_controller = ProjectListController()
        self._task_table_controller = TaskTableController(self._task_table_model)
        self._task_info_controller = TaskInfoController(self._task_table_model)

    @Property(QObject, constant=True)
    def project_list_controller(self):
        return self._project_list_controller

    @Property(QObject, constant=True)
    def task_table_controller(self):
        return self._task_table_controller

    @Property(QObject, constant=True)
    def task_info_controller(self):
        return self._task_info_controller
