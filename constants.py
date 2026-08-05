from PySide6.QtCore import Qt
from enum import IntEnum, auto


class TaskItemRoles(IntEnum):
    ID = Qt.ItemDataRole.UserRole + 1
    START_DATE = auto()
    END_DATE = auto()
    STATUS = auto()
    DESCRIPTION = auto()
    NAME = auto()
    TYPE = auto()
    PRIORITY = auto()
    PROJECT = auto()
    CREATION_DATE = auto()
    # COLOR = auto()


role_names: dict = {
    TaskItemRoles.ID: b'id',
    TaskItemRoles.START_DATE: b'start_date',
    TaskItemRoles.END_DATE: b'end_date',
    TaskItemRoles.STATUS: b'status',
    TaskItemRoles.DESCRIPTION: b'description',
    TaskItemRoles.NAME: b'name',
    TaskItemRoles.TYPE: b'type',
    TaskItemRoles.PRIORITY: b'priority',
    TaskItemRoles.PROJECT: b'project',
    TaskItemRoles.CREATION_DATE: b'creation_date',
    # TaskItemRoles.COLOR: b'color',
}
