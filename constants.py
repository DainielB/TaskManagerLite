from PySide6.QtCore import Qt
from enum import IntEnum, Enum, auto


# VARIABLES
DATE_FORMAT: str = "yyyy-M-d"


class TaskItemRoles(IntEnum):
    ID = Qt.ItemDataRole.UserRole + 1
    START_DATE = auto()
    END_DATE = auto()
    STATUS = auto()
    DESCRIPTION = auto()
    NAME = auto()
    KIND = auto()
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
    TaskItemRoles.KIND: b'kind',
    TaskItemRoles.PRIORITY: b'priority',
    TaskItemRoles.PROJECT: b'project',
    TaskItemRoles.CREATION_DATE: b'creation_date',
    # TaskItemRoles.COLOR: b'color',
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
