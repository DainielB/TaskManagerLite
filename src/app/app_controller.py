from PySide6.QtCore import QObject, Property
from src.app.project_list_controller import ProjectListController


class AppController(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._project_list_controller = ProjectListController()

    @Property(QObject, constant=True)
    def project_list_controller(self):
        return self._project_list_controller
