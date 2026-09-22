from PySide6.QtCore import(
    Property,
    QObject,
    Slot,
)

from src.data.task import Task


class TaskTableController(QObject):

    def __init__(self, model, parent=None):
        super().__init__(parent)

        self._model = model
        self._selected_task_id: str = None

    @Property(QObject, constant=True)
    def task_table_model(self):
        return self._model

    @property
    def selected_task_id(self) -> str:
        return self._selected_task_id

    @selected_task_id.setter
    def selected_task_id(self, id: str) -> None:
        self._selected_task_id = id

    @Slot(str, str, str, str, str, str, str)
    def add_new_task(
        self,
        project_id: str,
        name: str,
        end_date: str,
        priority: str,
        kind: str,
        status: str = "",
        description: str = ""
    ) -> None:
        """
        Adds a task to the task table with the given info.
        """

        if not project_id:
            raise ValueError("A project must be selected before creating a new task.")

        new_task = Task(name, end_date, priority, kind, status, description, project_id)

        self._model.add_task(new_task, True)

    @Slot(str)
    def remove_task(self, task_id: str) -> None:
        """_summary_

        Args:
            task_id (str): _description_
        """

        self._model.remove_task(task_id)