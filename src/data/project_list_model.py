from PySide6.QtCore import (
    Qt,
    QAbstractListModel,
    QModelIndex,
    QPersistentModelIndex,
    Slot,
)

from constants import ProjectRoles, project_role_names, DATE_FORMAT
from src.data.project import Project
from src.data.project_repository import ProjectRepository


class ProjectsListModel(QAbstractListModel):

    def __init__(self):
        super().__init__()

        self._repository: ProjectRepository = ProjectRepository()
        self._projects: list = self._repository.get_all()

    @property
    def projects(self) -> list:
        return self._projects

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        Returns the number of rows under the given parent.
        When the parent is valid it means that rowCount is returning
        the number of children of parent.
        """

        return len(self._projects)

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex) -> int:
        return 1

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = Qt.DisplayRole):
        """Returns an appropriate value for the requested data.
        If the view requests an invalid index, an invalid variant is returned.
        Any valid index that corresponds to a string in the list causes that
        string to be returned."""

        if not index.isValid() or not (0 <= index.row() < len(self._projects)):
            return None

        if role not in list(project_role_names):
            return None

        project = self._projects[index.row()]

        if role == ProjectRoles.ID:
            return project.id
        elif role == ProjectRoles.NAME:
            return project.name
        elif role == ProjectRoles.DESCRIPTION:
            return project.description
        elif role == ProjectRoles.END_DATE:
            return project.end_dat
        elif role == ProjectRoles.START_DATE:
            return project.start_date
        elif role == ProjectRoles.CREATION_DATE:
            return project.creation_date
        elif role == ProjectRoles.STATUS:
            return project.status
        elif role == ProjectRoles.PROJECT:
            return project

        return None

    def roleNames(self) -> dict:
        return project_role_names

    @Slot(str)
    def add_project(self, project: Project) -> None:
    # def add_project(self, project: Project) -> None:
        """Adds a project to the project list at the specified index with the given name."""

        new_index = len(self._projects)

        if len(self._projects) == 0:
            new_index = 0

        self.beginInsertRows(QModelIndex(), new_index, new_index)
        # self._projects.insert(new_index, project)
        self._projects.append(project)
        self._repository.add(project)
        self.endInsertRows()
