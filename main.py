import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from src.ui.create_project_dialog import CreateProjectDialog
from src.ui.projects_list import ProjectsListModel
from src.ui.task_info import TaskInfo

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qml_file = Path(__file__).parent / "src/ui/MainView.qml"
    engine.load(QUrl.fromLocalFile(str(qml_file)))

    if not engine.rootObjects():
        sys.exit(-1)

    """
    task_info = TaskInfo()
    engine.rootContext().setContextProperty("taskInfo", task_info)

    project_dialog = CreateProjectDialog()
    engine.rootContext().setContextProperty("projectDialog", project_dialog)
    """

    sys.exit(app.exec())
