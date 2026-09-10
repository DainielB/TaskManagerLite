from PySide6.QtCore import (
    Property,
    QObject,
    Signal,
    Slot
)

from src.data.project_list_model import ProjectsListModel
from src.data.project import Project


class ProjectListController(QObject):

    projectCountChangedSignal = Signal(int)
    projectSelectedSignal = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        self._selected_project: Project = None
        self._project_list_model = ProjectsListModel()

    @property
    def selected_project(self) -> Project:
        return self._selected_project

    @selected_project.setter
    def selected_project(self, project: Project) -> None:
        self._selected_project = project
        self.projectSelectedSignal.emit(self._is_project_selected())

    def _is_project_selected(self) -> bool:
        """
        if self._selected_project is None:
            return False
        return self._selected_project.status != TaskStatus.IN_PROGRESS
        """
        return self._selected_project is not None
    
    projectSelected = Property(bool, _is_project_selected, notify=projectSelectedSignal)

    @Property(QObject, constant=True)
    def project_list_model(self):
        return self._project_list_model

    @Slot(str, str, str)
    def add_new_project(self, name: str, end_date: str, description: str) -> None:
        """
        Adds a project to the project list at the specified index with the given info.
        """

        new_project = Project(name, end_date, description)

        self._project_list_model.add_project(new_project)
        self.selected_project = new_project
        self.projectCountChangedSignal.emit(self.num_projects())

    def num_projects(self) -> int:
        return len(self.project_list_model.projects)

    projectCount = Property(int, num_projects, notify=projectCountChangedSignal)