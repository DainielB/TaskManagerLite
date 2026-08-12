from PySide6.QtCore import Qt
from enum import IntEnum, Enum, auto


# VARIABLES
DATE_FORMAT: str = "yyyy-M-d"


class TaskRoles(IntEnum):
    ID = Qt.ItemDataRole.UserRole + 1
    START_DATE = auto()
    END_DATE = auto()
    STATUS = auto()
    DESCRIPTION = auto()
    NAME = auto()
    KIND = auto()
    PRIORITY = auto()
    # PROJECT = auto()
    CREATION_DATE = auto()
    # COLOR = auto()


role_names: dict = {
    TaskRoles.ID: b'id',
    TaskRoles.START_DATE: b'start_date',
    TaskRoles.END_DATE: b'end_date',
    TaskRoles.STATUS: b'status',
    TaskRoles.DESCRIPTION: b'description',
    TaskRoles.NAME: b'name',
    TaskRoles.KIND: b'kind',
    TaskRoles.PRIORITY: b'priority',
    # TaskRoles.PROJECT: b'project',
    TaskRoles.CREATION_DATE: b'creation_date',
    # TaskRoles.COLOR: b'color',
}


class TaskStatus(Enum):
    IN_PROGRESS = "In Progress"
    IN_REVIEW = "In Review"
    TO_DO = "To Do"
    PAUSED = "Paused"
    BACKLOG = "Backlog"
    FINISHED = "Finished"


class TaskKind(Enum):
    MODELING = "Modeling"
    SHADING = "Shading"
    RIG = "Rig"
    LAYOUT = "Layout"
    ANIMATION = "Animation"
    FX = "FX"
    LIGHTING = "Lighting"
    COMPOSITING = "Compositing"


class TaskPriority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    URGENT = "Urgent"
