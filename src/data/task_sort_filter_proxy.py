from PySide6.QtCore import (
    Property,
    QDate,
    QSortFilterProxyModel,
    Slot,
    QModelIndex,
    Qt,
    QObject,
    QRegularExpression
)

from PySide6.QtQml import QmlElement

from constants import (
    COLUMN_NUM,
    TaskRoles,
    task_role_names,
    DATE_FORMAT,
)


QML_IMPORT_NAME = "TaskProxyModel"
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0

@QmlElement
class TaskSortFilterProxy(QSortFilterProxyModel):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._sort_role = TaskRoles.PRIORITY
        self._source_model = None
        self._status: str = None
        self._current_sort_field: str = "priority"
        self._search_text: str = ""

        self.setDynamicSortFilter(True)
        self.setSortCaseSensitivity(Qt.CaseSensitivity.CaseSensitive)
        self.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.setFilterKeyColumn(-1) # Search all columns

        self.setFilterRegularExpression(
            QRegularExpression(self._search_text, QRegularExpression.CaseInsensitiveOption)
        )

        self.setSortRole(self._sort_role)

    def get_source_model(self):
        return self._source_model

    def set_source_model(self, model):
        if not model:
            return

        self.setSourceModel(model)
        self._source_model = model

        self.sort(0, Qt.SortOrder.DescendingOrder)

    source_model = Property(QObject, fget=get_source_model, fset=set_source_model)

    def get_status(self):
        return self._status

    def set_status(self, new_status: str):
        self._status = new_status
        # self.invalidateFilter()

    status = Property(str, fget=get_status, fset=set_status)

    def lessThan(self, source_left: QModelIndex, source_right: QModelIndex) -> bool:
        model = self.get_source_model()
        left_data = model.data(source_left, self._sort_role)
        right_data = model.data(source_right, self._sort_role)
        sort_role: int = self.sortRole()

        if sort_role == TaskRoles.NAME:
            return str(left_data) < str(right_data)
        elif sort_role == TaskRoles.END_DATE:
            return QDate.fromString(left_data, DATE_FORMAT) < QDate.fromString(right_data, DATE_FORMAT)
        elif sort_role == TaskRoles.PRIORITY:
            return int(left_data) < int(right_data)
        elif sort_role == TaskRoles.KIND:
            return str(left_data) < str(right_data)

        return super().lessThan(source_left, source_right)

    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool:

        if not self._source_model:
            return False

        source_index = self._source_model.index(source_row, COLUMN_NUM, source_parent)

        # STATUS Filter
        status = self._source_model.data(source_index, TaskRoles.STATUS.value)

        if status != self._status:
            return False

        # TEXT Filter
        if self._search_text:
            name = self._source_model.data(source_index, TaskRoles.NAME) or ""
            if self._search_text.lower() not in str(name).lower():
                return False

        # return status == self._status
        return True

    @Slot(str)
    def set_sort_role(self, role: str) -> None:
        role_name = role.encode('utf-8')

        matches = [k for k, v in task_role_names.items() if v == role_name]
        if not matches:
            return

        self._sort_role: int = matches[0]
        self.setSortRole(self._sort_role)

        if self._current_sort_field == role:
            new_order = Qt.SortOrder.AscendingOrder if self.sortOrder() == Qt.SortOrder.DescendingOrder else Qt.SortOrder.DescendingOrder
        else:
            new_order = Qt.SortOrder.DescendingOrder

        self._current_sort_field = role
        self.sort(0, new_order)
        # self.invalidate()

    @Slot(str)
    def search_all_by(self, text_input: str) -> None:
        self._search_text = text_input
        self.invalidateFilter()
