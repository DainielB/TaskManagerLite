from PySide6.QtCore import QSortFilterProxyModel


class PausedProxy(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
