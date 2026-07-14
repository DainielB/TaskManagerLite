import typing
from dataclasses import fields

from PySide6.QtCore import (
    QAbstractListModel,
    QByteArray,
    QModelIndex,
    QObject,
    QPersistentModelIndex,
    Qt,
    Slot,
)


class ProjectsListModel(QAbstractListModel):

    def __init__(self):
        super().__init__()
        self._projects: list = []

    def rowCount(
        self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()
    ) -> int:
        """
        Returns the number of rows under the given parent.
        When the parent is valid it means that rowCount is returning
        the number of children of parent.
        """

        if parent.isValid():
            return 0

        return len(self._projects)

    def data(
        self,
        index: QModelIndex | QPersistentModelIndex,
        role: int = Qt.ItemDataRole.DisplayRole,
    ) -> typing.Any:
        """Returns an appropriate value for the requested data.
        If the view requests an invalid index, an invalid variant is returned.
        Any valid index that corresponds to a string in the list causes that
        string to be returned."""

        if not index.isValid() < self.rowCount():
            project = self._projects[index.row()]
            name = self.roleNames().get(role)
            if name:
                return
                # return getattr(project, name.data().decode())

    """
    def roleNames(self) -> dict[int, QByteArray]:
        d = {}
        for i, field in enumerate(fields(Project)):
            d[Qt.ItemDataRole.DisplayRole + i] = field.name.encode()
        return d
    """

    @Slot(list)
    def add_project(self, project) -> None:
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._projects.insert(self.rowCount(), project)
        self.endInsertRows()

    """
    @Slot(result=list)
    def get_projects(self) -> list:
        return self._projects

    @Slot(result=int)
    def num_projects(self) -> int:
        return len(self._projects)
    """
