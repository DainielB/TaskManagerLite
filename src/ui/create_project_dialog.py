from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtQml import QmlElement

QML_IMPORT_NAME = "TaskManagerLite"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class CreateProjectDialog(QObject):

    acceptSignal = Signal(dict)
    cancelSignal = Signal()

    def __init__(self, parent=QObject | None):
        super().__init__()

    @Slot(list, result=dict)
    def on_accept(self, info: list):
        # self.acceptSignal.emit(self._project_data)
        # self.acceptSignal.emit({"name": info[0], "description": info[1], "endDate": info[2], "color": info[3]})
        print({"name": info[0], "description": info[1], "endDate": info[2], "color": info[3]})
        #return {"name": info[0], "description": info[1], "endDate": info[2], "color": info[3]}

    @Slot()
    def on_cancel(self):
        # self.cancelSignal.emit()
        print("ON CANCEL")
        pass
