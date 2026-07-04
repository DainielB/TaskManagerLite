from PySide6.QtCore import QObject, Signal, Slot


class TaskInfo(QObject):
    taskEdited = Signal()

    def __init__(self):
        super().__init__()

    @Slot(QObject, list)
    def edit_button_released(self, button, controls: list):
        """
        Enables the controls in the given list.

        Args:
            controls (list): A list of controls to enable.
        """

        text: str = button.property("text")
        button.setProperty("text", "Save" if text == "Edit" else "Edit")

        for button in controls:
            enabled: bool = button.property("enabled")
            button.setProperty("enabled", not enabled)
        # self.taskEdited.emit()
