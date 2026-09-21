from PySide6.QtCore import (
    Qt,
    QAbstractListModel,
    QModelIndex,
    QPersistentModelIndex,
    Slot,
    Signal
)

from constants import ProjectRoles, project_role_names, DATE_FORMAT
from src.data.project import Project
from src.data.project_repository import ProjectRepository


class ProjectsListModel(QAbstractListModel):

    numProjectsChanged = Signal(int)

    def __init__(self):
        super().__init__()

        self._repository: ProjectRepository = ProjectRepository()
        self._projects: list = self._repository.get_all()

    @property
    def repository(self) -> ProjectRepository:
        return self._repository

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
    def add_project(self, project: Project, insert: bool = False) -> None:
        """Adds a project to the project list at the specified index with the given name.

        Args:
            project (Project): _description_
        """

        new_index = len(self._projects)

        if len(self._projects) == 0:
            new_index = 0

        self.beginInsertRows(QModelIndex(), new_index, new_index)
        # self._projects.insert(new_index, project)
        self._projects.append(project)
        self.endInsertRows()

        if insert:
            self.repository.add(project)

        self.numProjectsChanged.emit(len(self._projects))

    def _delete_project(self, _id: str) -> None:
        """_summary_

        Args:
            _id (str): id of the project selected
        """

        if len(self._projects) > 0:
            removed_rows = []

            for row, project in enumerate(self._projects):
                if project in self._projects:
                    removed_rows.append(row)

            for row in sorted(removed_rows, reverse=True):
                self.beginRemoveRows(QModelIndex(), row, row)
                self._projects.pop(row)
                self.endRemoveRows()

            self.repository.delete_tasks_by_project_id(_id)
            self.repository.delete(_id)
            self.__refresh_table(_id)

    def __refresh_table(self, project_id: str = None) -> None:
        """_summary_

        Args:
            project_id (str, optional): _description_. Defaults to None.
        """

        projects_list: list = self.repository.get_all()
        for project in projects_list:
            self.add_project(project)