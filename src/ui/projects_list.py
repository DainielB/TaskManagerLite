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


@QmlElement
class ProjectsListModel(QAbstractListModel):
    def __init__(self, parent=QObject | None):
        super().__init__()
        self._projects: list[Project] = []

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

    def add_student(self, project: Project) -> None:
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._projects.append(project)
        self.endInsertRows()

    """
    @Slot(str)
    def add_project(self, project_name: str):
        self._projects.append(project_name)
    """

    @Slot()
    def get__projects(self):
        return self._projects

    @Slot(result=int)
    def num__projects(self):
        return len(self._projects)

    """
    @Slot(int, result=str)
    def get_project_name(self, index: int) -> str:
        return self._projects[index]
    """
