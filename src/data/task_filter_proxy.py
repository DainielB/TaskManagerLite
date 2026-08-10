from PySide6.QtCore import (
    QDate,
    QSortFilterProxyModel,
    Slot,
    QModelIndex,
    Qt,
)

from constants import TaskItemRoles, TaskStatus, role_names


class TaskFilterProxy(QSortFilterProxyModel):

    def __init__(self, status: TaskStatus, source_model, parent=None):
        super().__init__(parent)

        self._sort_role = None
        self._filter_role = None
        self._source_column: int = 0
        self._general_status: TaskStatus = status

        self.setSourceModel(source_model)
        self.setDynamicSortFilter(True)
        self.setSortCaseSensitivity(Qt.CaseSensitive)
        self.setFilterCaseSensitivity(Qt.CaseInsensitive)

    @Slot(str, int)
    def set_sort_role(self, role: str, source_column: int):
        role_name = role.encode('utf-8')
        self._sort_role: int = [k for k, v in role_names.items() if v == role_name][0]
        self.setSortRole(self._sort_role)
        # self.sortRoleChanged.emit(self._sort_role)
        self.sort(source_column)
        # self.invalidate()

    @Slot(str, int)
    def set_filter_role(self, role: str, source_column: int):
        self._filter_role = role.encode('utf-8')
        '''
        filter_index: int = [k for k, v in role_names.items() if v == self._sort_role][0]
        self.setFilterRole(role_index)
        self.sort(source_column)
        '''

    def lessThan(self, source_left: QModelIndex, source_right: QModelIndex) -> bool:
        print(f"Comparing: {source_left.data(self._sort_role)}, {source_right.data(self._sort_role)}")

        print(f"sortRole: {self.sortRole()}")

        model = self.sourceModel()
        left_data = model.data(source_left, self._sort_role)
        right_data = model.data(source_right, self._sort_role)

        print(f"left_data: {left_data}, right_data: {right_data}")

        if self.sortRole() == TaskItemRoles.END_DATE:
            return QDate.fromString(left_data, Qt.DateFormat.ISODate) < QDate.fromString(right_data, Qt.DateFormat.ISODate)
        elif self.sortRole() == TaskItemRoles.NAME:
            return str(left_data).lower() < str(right_data).lower()
        else:
            # elif self.sortRole() == TaskItemRoles.PRIORITY:
            return left_data < right_data

    def filterAcceptsColumn(self, source_column: int, source_parent: QModelIndex) -> bool:
        # left_data = self.sourceModel().data(left, Qt.ItemDataRole.DisplayRole)
        # right_data = self.sourceModel().data(right, Qt.ItemDataRole.DisplayRole)

        return True

    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool:
        model = self.sourceModel()
        index = model.index(source_row, 0, source_parent)
        task_status = model.data(index, TaskItemRoles.STATUS)

        return task_status == self._general_status
