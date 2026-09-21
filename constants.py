from PySide6.QtCore import Qt
from enum import (
    IntEnum,
    Enum,
    auto,
)
from pathlib import Path


### VARIABLES###
DATE_FORMAT: str = "yyyy-M-d"
COLUMN_NUM: int = 0
# Database
_DB_NAME: str = ".db"
_current_file: Path = Path(__file__).resolve()
_project_root: Path = _current_file.parent / ".db"
DB_PATH: Path = _project_root / _DB_NAME


class ProjectRoles(IntEnum):
    ID = Qt.ItemDataRole.UserRole + 1
    NAME = auto()
    DESCRIPTION = auto()
    END_DATE = auto()
    START_DATE = auto()
    CREATION_DATE = auto()
    STATUS = auto()
    PROJECT = auto()

project_role_names = {
    ProjectRoles.ID: b'id',
    ProjectRoles.NAME: b'name',
    ProjectRoles.DESCRIPTION: b'description',
    ProjectRoles.END_DATE: b'end_date',
    ProjectRoles.START_DATE: b'start_date',
    ProjectRoles.CREATION_DATE: b'creation_date',
    ProjectRoles.STATUS: b'status',
}


class ProjectStatus(Enum):
    READY_TO_START = "Ready to Start"
    IN_PROGRESS = "In Progress"
    FINISHED = "Finished"


class TaskRoles(IntEnum):
    ID = Qt.ItemDataRole.UserRole + 1
    START_DATE = auto()
    END_DATE = auto()
    STATUS = auto()
    DESCRIPTION = auto()
    NAME = auto()
    KIND = auto()
    PRIORITY = auto()
    COLOR = auto()
    CREATION_DATE = auto()
    TASK = auto()

task_role_names: dict = {
    TaskRoles.ID: b'id',
    TaskRoles.START_DATE: b'start_date',
    TaskRoles.END_DATE: b'end_date',
    TaskRoles.STATUS: b'status',
    TaskRoles.DESCRIPTION: b'description',
    TaskRoles.NAME: b'name',
    TaskRoles.KIND: b'kind',
    TaskRoles.PRIORITY: b'priority',
    TaskRoles.COLOR: b'color',
    TaskRoles.CREATION_DATE: b'creation_date',
    TaskRoles.TASK: b'task',
}


class TaskStatus(Enum):
    # INITIAL_STATUS = "Initial Status"
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

class TaskPriority(IntEnum):
    Low = 0
    Medium = 1
    High = 2
    Urgent = 3

class TaskPriorityColor(Enum):
    Low = "#4DAA57" #78A1BB #1098F7
    Medium = "#F0803C"
    High = "#A10702" #95190C
    Urgent = "#731DD8" #6622CC #545775 #731DD8