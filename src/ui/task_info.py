from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


class TaskInfo(QObject):
    editTaskSignal = Signal()

    def __init__(self):
        super().__init__()

    @Slot()
    def on_button_released(self):
        print("¡Botón soltado desde Python!")
        # self.editTaskSignal.emit()
