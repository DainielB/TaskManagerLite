import QtQuick.Window
import QtQuick.Layouts
import QtQuick.Controls


Window {
    id: mainWindow

    color: "black"
    width: 800
    height: 600
    visible: true
    title: "Task Manager Lite"

    minimumWidth: 400
    minimumHeight: 300

    ColumnLayout {
        anchors.fill: parent

        GridLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            columns: 10

            ProjectsList {
                id: projects
                projectName: "Project Test"
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.preferredWidth: 1
            }

            TasksList {
                id: tasksList
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.preferredWidth: 4
            }

            TaskInfo {
                id: tasks
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.preferredWidth: 2
            }

        }

    }

    CreateProjectDialog {
        id: projectDialog
    }
}
