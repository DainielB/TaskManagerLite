from PySide6.QtCore import Property, QObject, Slot

from src.data.project_list_model import ProjectsListModel
from src.data.project import Project


class ProjectListController(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._project_list_model = ProjectsListModel()

    @Property(QObject, constant=True)
    def project_list_model(self):
        return self._project_list_model

    @Slot(str, str, str, str)
    def add_new_project(self, name: str, end_date: str, description: str) -> None:
        """
        Adds a project to the project list at the specified index with the given info.
        """

        new_project = Project(name, end_date, description)

        self._project_list_model.add_project(new_project.name)
