from uuid import UUID

from PySide6.QtCore import(
    QObject,
    Signal,
    Slot,
    Qt
)

from src.data.task import Task


class TaskInfoController(QObject):

    taskClicked = Signal("QVariant")

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
    def load_task(self, id: UUID) -> None:
        task = self._model.get_task_by_id(id)

        self.selected_task = task

        self.taskClicked.emit(task)
