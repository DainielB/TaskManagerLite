from uuid import UUID

from PySide6.QtCore import(
    QDate,
    QObject,
    Signal,
    Slot,
    Qt
)

from constants import DATE_FORMAT, TaskKind, TaskPriority, TaskRoles, TaskStatus
from src.data.task import Task


class TaskInfoController(QObject):

    taskClicked = Signal("QVariant")
    taskEdited = Signal("QVariant")
    # statusModified = Signal(str)

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

    @Slot(UUID)
    def load_task(self, id) -> None:
        task = self._model.get_task_by_id(id)
        self.selected_task = task
        task_dict = {
            TaskRoles.ID.name: str(task.id),
            TaskRoles.NAME.name: str(task.name),
            TaskRoles.DESCRIPTION.name: str(task.description),
            TaskRoles.END_DATE.name: QDate.toString(task.end_date, DATE_FORMAT),
            TaskRoles.STATUS.name: str(task.status.value),
            TaskRoles.KIND.name: str(task.kind.value),
            TaskRoles.PRIORITY.name: str(task.priority.value)
        }

        self.taskClicked.emit(task_dict)

    @Slot(str, str, str, str, str, str)
    def save_task(self, name: str, description: str, end_date: str, status: str, kind: str, priority: str) -> None:

        if name != self.selected_task.name:
            self.selected_task.name = name

        if description != self.selected_task.description:
            self.selected_task.description = description

        if end_date != self.selected_task.end_date.toString(DATE_FORMAT):
            self.selected_task.end_date = QDate.fromString(end_date, DATE_FORMAT)

        if TaskStatus(status) != self.selected_task.status:
            self.selected_task.status = TaskStatus(status)

        if TaskKind(kind) != self.selected_task.kind:
            self.selected_task.kind = TaskKind(kind)

        if TaskPriority(priority) != self.selected_task.priority:
            self.selected_task.priority = TaskPriority(priority)

        print(self.selected_task)

    def _has_changed(self, new_value, old_value) -> bool:
        """
        Checks if any change exists for not to connect with the database if not necessary.
        """
        return new_value != old_value
