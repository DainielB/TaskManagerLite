import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle

from src.app.app_controller import AppController
from src.app.validator import Validator


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    QQuickStyle.setStyle("Universal")

    qml_app_engine = QQmlApplicationEngine()
    qml_context = qml_app_engine.rootContext()

    # Main controller
    app_controller = AppController(parent=app)
    qml_app_engine.rootContext().setContextProperty("app_controller", app_controller)

    # Validators
    validator = Validator()
    qml_app_engine.rootContext().setContextProperty("input_validator", validator)

    date_validator = Validator()
    qml_app_engine.rootContext().setContextProperty("date_validator", date_validator)

    current_file_path = Path(__file__)
    main_qml_path = current_file_path.parent / 'src/ui/MainView.qml'
    qml_app_engine.load(QUrl.fromLocalFile(str(main_qml_path)))

    if len(qml_app_engine.rootObjects()) == 0:
        sys.exit('Failed to start the UI.')

    sys.exit(app.exec())
