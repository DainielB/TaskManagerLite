from PySide6.QtCore import QSortFilterProxyModel


class BacklogProxy(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
