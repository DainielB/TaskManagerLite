from PySide6.QtCore import QSortFilterProxyModel

from QtCore import StatusRole


class TaskFilterProxy(QSortFilterProxyModel):
    def __init__(self, status, source_model, parent=None):
        super().__init__(parent)
        self.setSourceModel(source_model)
        self._status = status

    def filterAcceptsRow(self, source_row, source_parent):
        index = self.sourceModel().index(source_row, 0, source_parent)
        return self.sourceModel().data(index, StatusRole) == self._status
