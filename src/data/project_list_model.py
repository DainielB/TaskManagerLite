import typing
from enum import IntEnum, auto

from PySide6.QtCore import (
    Qt,
    QAbstractListModel,
    QModelIndex,
    QPersistentModelIndex,
    Slot,
)


class ProjectItemRoles(IntEnum):
    ID = Qt.ItemDataRole.UserRole + 1
    NAME = auto()
    DESCRIPTION = auto()
    END_DATE = auto()
    START_DATE = auto()
    CREATION_DATE = auto()
    STATE = auto()
    COLOR = auto()


_role_names = {
    ProjectItemRoles.ID: b'id',
    ProjectItemRoles.NAME: b'name',
    ProjectItemRoles.DESCRIPTION: b'description',
    ProjectItemRoles.END_DATE: b'end_date',
    ProjectItemRoles.START_DATE: b'start_date',
    ProjectItemRoles.CREATION_DATE: b'creation_date',
    ProjectItemRoles.STATE: b'state',
    ProjectItemRoles.COLOR: b'color',
}


class ProjectsListModel(QAbstractListModel):

    def __init__(self):
        super().__init__()
        self._projects: list = []

        self.add_project("Test Project 1")

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        """
        Returns the number of rows under the given parent.
        When the parent is valid it means that rowCount is returning
        the number of children of parent.
        """

        if parent.isValid():
            return 0

        return len(self._projects)

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = Qt.DisplayRole) -> typing.Any:
        """Returns an appropriate value for the requested data.
        If the view requests an invalid index, an invalid variant is returned.
        Any valid index that corresponds to a string in the list causes that
        string to be returned."""

        if role not in list(_role_names):
            return None

        try:
            project = self._projects[index.row()]
        except IndexError:
            return None

        if role in project:
            return project[role]

        return None

    def roleNames(self) -> dict:
        return _role_names

    @Slot(str)
    def add_project(self, project_name: str) -> None:
        """Adds a project to the project list at the specified index with the given name."""

        if len(self._projects) == 0:
            new_index = 0
        else:
            new_index = len(self._projects)

        new_project = { ProjectItemRoles.NAME: project_name }

        self.beginInsertRows(QModelIndex(), new_index, new_index)
        self._projects.insert(new_index, new_project)
        self.endInsertRows()
