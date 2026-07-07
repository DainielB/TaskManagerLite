import sys
from pathlib import Path

from create_project_dialog import CreateProjectDialog
from projects_list import ProjectsList
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# from tasks_list import TasksList
from task_info import TaskInfo

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qml_file = Path(__file__).parent / "main.qml"
    engine.load(QUrl.fromLocalFile(str(qml_file)))

    if not engine.rootObjects():
        sys.exit(-1)

    # projects_list = ProjectsList()
    # engine.rootContext().setContextProperty("projectsList", projects_list)

    # tasks_list = tasks_list.TasksList()
    # engine.rootContext().setContextProperty("tasksList", tasks_list)

    task_info = TaskInfo()
    engine.rootContext().setContextProperty("taskInfo", task_info)

    project_dialog = CreateProjectDialog()
    engine.rootContext().setContextProperty("projectDialog", project_dialog)

    sys.exit(app.exec())
