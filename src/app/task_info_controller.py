from PySide6.QtCore import(
    Property,
    QDate,
    QObject,
    Slot,
    Qt
)

from constants import TaskStatus
from src.data.task_table_model import TaskTableModel
from src.data.task import Task


class TaskInfoController(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)
