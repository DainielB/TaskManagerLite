from PySide6.QtCore import QSortFilterProxyModel, Slot, QModelIndex

from constants import TaskItemRoles, role_names


class TaskFilterProxy(QSortFilterProxyModel):

    # def __init__(self, status, source_model, parent=None):
    def __init__(self, source_model, parent=None):
        super().__init__(parent)

        self._filter_role = None
        self._source_column: int = 0

        self.setSourceModel(source_model)
        self.setDynamicSortFilter(True)
        # self._status = status

    @Slot(str, int)
    def set_sort_role(self, role: str, source_column: int):
        self._sort_role = role.encode('utf-8')
        print(f"[k for k, v in role_names.items() if v == self._filter_role] -> {[k for k, v in role_names.items() if v == self._sort_role]}")
        role_index: int = [k for k, v in role_names.items() if v == self._sort_role][0]
        self.setSortRole(role_index)
        print("Filter role set to:", role_index)
        self.sort(source_column)
        # self.invalidateFilter()

    def filterAcceptsColumn(self, source_column: int, source_parent: QModelIndex) -> bool:
        # left_data = self.sourceModel().data(left, Qt.ItemDataRole.DisplayRole)
        # right_data = self.sourceModel().data(right, Qt.ItemDataRole.DisplayRole)

        return True
