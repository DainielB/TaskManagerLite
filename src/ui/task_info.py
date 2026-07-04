from tkinter.constants import S

from PySide6.QtCore import QObject, Signal, Slot


class TaskInfo(QObject):
    taskEdited = Signal()

    def __init__(self):
        super().__init__()

    @Slot(QObject, list)
    def edit_button_released(self, edit_button: QObject, controls: list):
        """
        Enables the controls in the given list.

        Args:
            edit_button (QObject): The edit button to update.
            controls (list): A list of controls to enable.
        """

        text: str = edit_button.property("text")
        edit_button.setProperty("text", "Save" if text == "Edit" else "Edit")

        for button in controls:
            enabled: bool = button.property("enabled")
            button.setProperty("enabled", not enabled)
        # self.taskEdited.emit()

    @Slot(QObject, QObject, list)
    def cancel_button_released(
        self, edit_button: QObject, cancel_button: QObject, controls: list
    ):
        """
        Disables the controls in the given list and reverts the edit button text.

        Args:
            edit_button (QObject): The edit button to update.
            controls (list): A list of controls to enable.
        """

        text: str = edit_button.property("text")
        edit_button.setProperty("text", "Edit" if text == "Save" else "Edit")

        cancel_enabled: bool = cancel_button.property("enabled")
        cancel_button.setProperty("enabled", not cancel_enabled)

        for button in controls:
            button.setProperty("enabled", False)
