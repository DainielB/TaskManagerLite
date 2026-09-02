from PySide6.QtCore import (
    Property,
    QDate,
    QSortFilterProxyModel,
    Slot,
    QModelIndex,
    Qt,
    QObject
)

from constants import COLUMN_NUM, TaskRoles, role_names, COLUMN_NUM


class TaskFilterProxy(QSortFilterProxyModel):

    # def __init__(self, status: TaskStatus, source_model, parent=None):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._sort_role = None
        self._filter_role = None
        self._source_column: int = 0
        self._source_model = None
        self._status: str = None

        self.setDynamicSortFilter(True)
        self.setSortCaseSensitivity(Qt.CaseSensitive)
        self.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.setFilterKeyColumn(-1) # Search all columns

    def set_source_model(self, model):
        if not model:
            return

        self.setSourceModel(model)
        self._source_model = model

    source_model = Property(QObject, fget=lambda self: self.source_model, fset=set_source_model)

    def set_status(self, new_status: str):
        self._status = new_status

    status = Property(str, fget= lambda self: self.status, fset=set_status)

    @Slot(str, int)
    def set_sort_role(self, role: str, source_column: int):
        role_name = role.encode('utf-8')
        self._sort_role: int = [k for k, v in role_names.items() if v == role_name][0]
        self.setSortRole(self._sort_role)
        # self.sortRoleChanged.emit(self._sort_role)
        self.sort(source_column)
        # self.invalidate()

    '''
    @Slot(str, int)
    def set_filter_role(self, role: str, source_column: int):
        self._filter_role = role.encode('utf-8')
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
        sort_role: int = self.sortRole()

        print(f"left_data: {left_data}, right_data: {right_data}")

        if sort_role == TaskRoles.END_DATE:
            return QDate.fromString(left_data, Qt.DateFormat.ISODate) < QDate.fromString(right_data, Qt.DateFormat.ISODate)
        elif sort_role == TaskRoles.NAME:
            return str(left_data).lower() < str(right_data).lower()
        else:
            # elif sort_role == TaskRoles.PRIORITY:
            return left_data < right_data

    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool:
        source_index = self._source_model.index(source_row, COLUMN_NUM, source_parent)
        # source_index = self.sourceModel().index(source_row, COLUMN_NUM, source_parent)
        status = self._source_model.data(source_index, TaskRoles.STATUS)

        return status == self._status
