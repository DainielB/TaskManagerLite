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

        if self._project_list_model.projects:
            self._selected_project = self._project_list_model.projects[0]

        """
        __projects_list: list = self._project_list_model.projects
        self._selected_project: Project = None if len(__projects_list) == 0 else __projects_list[0]
        """

    @property
    def selected_project(self) -> Project:
        return self._selected_project

    @selected_project.setter
    def selected_project(self, project: Project) -> None:
        self._selected_project = project
        self.projectSelectedSignal.emit(self._is_project_selected())

    def _is_project_selected(self) -> bool:
        return self._selected_project is not None
    
    projectSelected = Property(bool, _is_project_selected, notify=projectSelectedSignal)

    def _selected_project_id(self) -> str:
            if self._selected_project is None:
                return None
            return self.selected_project.id
    
    selected_project_id = Property(str, _selected_project_id, notify=projectSelectedSignal)

    @Property(QObject, constant=True)
    def project_list_model(self):
        return self._project_list_model

    @Slot(int)
    def select_project(self, index: int) -> None:
        if not 0 <= index < len(self._project_list_model.projects):
            return

        self.selected_project = self._project_list_model.projects[index]

    @Slot(str, str, str)
    def add_new_project(self, name: str, end_date: str, description: str) -> None:
        """
        Adds a project to the project list at the specified index with the given info.
        """

        print(f"NAME: {name}")
        print(f"END DATE: {end_date}")
        print(f"DESCRIPTION: {description}")

        new_project = Project(name, end_date, description)

        self._project_list_model.add_project(new_project)
        self.selected_project = new_project
        self.projectCountChangedSignal.emit(self.num_projects())

    def num_projects(self) -> int:
        return len(self.project_list_model.projects)

    projectCount = Property(int, num_projects, notify=projectCountChangedSignal)