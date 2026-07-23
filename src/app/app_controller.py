from PySide6.QtCore import QObject, Property
from src.app.project_list_controller import ProjectListController
from src.app.task_table_controller import TaskTableController


class AppController(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._project_list_controller = ProjectListController()
        self._task_table_controller = TaskTableController()

    @Property(QObject, constant=True)
    def project_list_controller(self):
        return self._project_list_controller

    @Property(QObject, constant=True)
    def task_table_controller(self):
        return self._task_table_controller
