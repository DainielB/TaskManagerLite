from PySide6.QtCore import (
    Property,
    QObject,
    Signal,
    Slot
)

from src.data.project_list_model import ProjectsListModel
from src.data.project import Project


class ProjectListController(QObject):

    hasProjectChanged = Signal(bool)
    onProjectSelection = Signal(bool)
    # selectProjectSignal = Signal("QVariant")

    def __init__(self, parent=None):
        super().__init__(parent)

        self._selected_project: Project = None
        self._project_list_model = ProjectsListModel()

        if self._project_list_model.projects:
            self._selected_project = self._project_list_model.projects[0]
            self._project_list_model.numProjectsChanged.connect(self._on_project_count_changed)
        else:
            self._selected_project = None

    @property
    def selected_project(self) -> Project:
        return self._selected_project

    @selected_project.setter
    def selected_project(self, project: Project) -> None:
        self._selected_project = project
        # self.selectProjectSignal.emit(self._selected_project)

    """
    def _get_selected_project(self) -> Project:
        return self._selected_project
    """

    # selectedProject = Property("QVariant", fget=_get_selected_project, notify=selectProjectSignal)
    
    def _selected_project_id(self) -> str:
        if self._selected_project is None:
            return None

        return self.selected_project.id
    
    selected_project_id = Property(str, _selected_project_id, notify=onProjectSelection)

    @Property(QObject, constant=True)
    def project_list_model(self):
        return self._project_list_model

    @Slot(int)
    def select_project(self, index: int) -> None:
        """_summary_

        Args:
            index (int): _description_
        """

        if not 0 <= index < len(self._project_list_model.projects):
            return

        self.selected_project = self._project_list_model.projects[index]
        self.onProjectSelection.emit(True)

    @Slot(str, str, str)
    def add_new_project(self, name: str, end_date: str, description: str) -> None:
        """
        Adds a project to the project list at the specified index with the given info.
        """

        new_project = Project(name, end_date, description)

        self._project_list_model.add_project(new_project, True)
        self.selected_project = new_project

        self.hasProjectChanged.emit(self._has_projects())

    @Slot(str)
    def delete_project(self, id: str) -> None:
        """_summary_

        Args:
            id (str): _description_
        """

        self.project_list_model._delete_project(id)
        self.hasProjectChanged.emit(self._has_projects())

    def _has_projects(self) -> bool:
        return len(self.project_list_model.projects) > 0

    def _on_project_count_changed(self) -> None:
        self.hasProjectChanged.emit(self._has_projects())

    hasProjects = Property(bool, fget=_has_projects, notify=hasProjectChanged)