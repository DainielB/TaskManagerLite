from uuid import UUID

from PySide6.QtCore import(
    Property,
    QObject,
    Signal,
    Slot,
)

from src.data.task import Task


class TaskTableController(QObject):

    def __init__(self, model, parent=None):
        super().__init__(parent)

        self._model = model
        self._selected_task_id: UUID = None

    @Property(QObject, constant=True)
    def task_table_model(self):
        return self._model

    @property
    def selected_task_id(self) -> UUID:
        return self._selected_task_id

    @selected_task_id.setter
    def selected_task_id(self, id: UUID) -> None:
        self._selected_task_id = id

    @Slot(str, str, str, str, str, str)
    def add_new_task(self, name: str, end_date: str, priority: str, kind: str, status: str = "", description: str = "") -> None:
        """
        Adds a task to the task table with the given info.
        """
        new_task = Task(name, end_date, priority, kind, status, description)

        self._model.add_task(new_task)
