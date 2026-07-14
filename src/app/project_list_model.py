'''
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
from PySide6.QtQml import QmlElement

from src.data.project import Project

QML_IMPORT_NAME = "TaskManagerLite"
QML_IMPORT_MAJOR_VERSION = 1


# @QmlElement
class ProjectsListModel(QAbstractListModel):

    def __init__(self, parent=QObject | None):
        super().__init__()
        self._projects: list[Project] = []
        # self._projects: list[str] = []

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

    def roleNames(self) -> dict[int, QByteArray]:
        d = {}
        for i, field in enumerate(fields(Project)):
            d[Qt.ItemDataRole.DisplayRole + i] = field.name.encode()
        return d

    @Slot(list)
    def add_project(self, info: list[str]) -> None:
        print("AQUÍ ESTAMOS")
        self.beginInsertRows(QModelIndex(), 0, 0)
        project = Project(*info)
        self._projects.insert(0, project)
        #self._projects.append(project.name)
        print(self._projects)
        # self.insertRows(self.rowCount() - 1, 1, QModelIndex())
        self.endInsertRows()

    @Slot()
    def get__projects(self):
        return self._projects

    @Slot(result=int)
    def num__projects(self):
        return len(self._projects)

'''
