from uuid import UUID

from PySide6.QtCore import(
    Property,
    QDate,
    QObject,
    Signal,
    Slot,
)

from constants import (
    DATE_FORMAT,
    TaskKind,
    TaskPriority,
    TaskRoles,
    TaskStatus,
)
from src.data.task import Task


class TaskInfoController(QObject):

    taskClicked = Signal("QVariant")
    taskSelectedSignal = Signal(bool)

    nameChanged = Signal(str)
    descriptionChanged = Signal(str)
    endDateChanged = Signal(QDate)
    statusChanged = Signal(str)
    kindChanged = Signal(str)
    priorityChanged = Signal(str)

    def __init__(self, model, parent=None):
        super().__init__(parent)

        self._model = model
        self._selected_task: Task = None

    @property
    def selected_task(self) -> Task:
         return self._selected_task

    @selected_task.setter
    def selected_task(self, task: Task) -> None:
         self._selected_task = task
         self.taskSelectedSignal.emit(self._is_task_selected())

    def _is_task_selected(self) -> bool:
        if self._selected_task is None:
            return False
        return self._selected_task.status != TaskStatus.IN_PROGRESS

    taskSelected = Property(bool, _is_task_selected, notify=taskSelectedSignal)

    @Slot(str)
    def load_task(self, id) -> None:
        task: Task = self._model.get_task_by_id(id)
        self.selected_task = task
        task_dict = {
            TaskRoles.ID.name: str(task.id),
            TaskRoles.NAME.name: str(task.name),
            TaskRoles.DESCRIPTION.name: str(task.description),
            TaskRoles.END_DATE.name: QDate.toString(task.end_date, DATE_FORMAT),
            TaskRoles.STATUS.name: str(task.status.value),
            TaskRoles.KIND.name: str(task.kind.value),
            TaskRoles.PRIORITY.name: str(task.priority.name)
        }

        self.taskClicked.emit(task_dict)

    @Slot(str, str, str, str, str, str)
    def save_task(self, new_name: str = "", new_description: str = "", new_end_date: str = "", new_status: str = "", new_kind: str = "", new_priority: str = "") -> None:

        if not self.selected_task:
            return

        if new_name != self.selected_task.name:
            self.selected_task.name = new_name
            self.nameChanged.emit(new_name)

        if new_description != self.selected_task.description:
            self.selected_task.description = new_description
            self.descriptionChanged.emit(new_description)

        if new_end_date != self.selected_task.end_date.toString(DATE_FORMAT):
            self.selected_task.end_date = QDate.fromString(new_end_date, DATE_FORMAT)
            self.endDateChanged.emit(new_end_date)

        if TaskStatus(new_status) != self.selected_task.status:
            self.selected_task.status = TaskStatus(new_status)
            self.statusChanged.emit(new_status)
            self.taskSelectedSignal.emit(self._is_task_selected())

        if TaskKind(new_kind) != self.selected_task.kind:
            self.selected_task.kind = TaskKind(new_kind)
            self.kindChanged.emit(new_kind)

        if TaskPriority(new_priority) != self.selected_task.priority.name:
            self.selected_task.priority = TaskPriority(new_priority)
            self.priorityChanged.emit(new_priority)

        self._set_data()

    @Slot()
    def start_task(self) -> None:
        self._selected_task.status = TaskStatus.IN_PROGRESS
        self._set_data()
        self.load_task(self._selected_task.id)

    def _set_data(self) -> None:
        index = self._model.get_index_task(self.selected_task.id)
        self._model.setData(index, self.selected_task, TaskRoles.ID)
