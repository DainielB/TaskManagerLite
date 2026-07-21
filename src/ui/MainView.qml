import QtQuick.Window
import QtQuick.Layouts
import QtQuick.Controls


ApplicationWindow {
    property int totalParts: 10
    property int projectsListParts: 1
    property int tasksListParts: 6
    property int taskInfoParts: 3

    property int _padding: 5

    id: mainWindow

    color: "#30332E"
    width: 800
    height: 600
    visible: true
    title: "Task Manager Lite"
    leftPadding: _padding
    topPadding: _padding
    rightPadding: _padding
    bottomPadding: _padding

    minimumWidth: 400
    minimumHeight: 300

    ColumnLayout {
        anchors.fill: parent

        RowLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            spacing: 5

            ProjectsListView {
                id: projectsListView
                Layout.fillHeight: true
                Layout.preferredWidth: mainWindow.width * projectsListParts / mainWindow.totalParts
            }

            TasksListView {
                id: tasksList
                Layout.fillWidth: true
                Layout.fillHeight: true
                Layout.preferredWidth: mainWindow.width * tasksListParts / mainWindow.totalParts
            }

            TaskInfoView {
                id: tasks
                Layout.fillWidth: true
                Layout.fillHeight: true
                Layout.preferredWidth: mainWindow.width * taskInfoParts / mainWindow.totalParts
            }

        }

    }

    Loader {
        id: dialogLoader
        active: false

        sourceComponent: Component {
            CreateProjectView {
                id: projectDialog
                onAccepted: app_controller.project_list_controller.add_new_project(projectDialog.projectName, projectDialog.projectDescription, projectDialog.limitDateInput.dateInput, projectDialog.projectColor)
                onClosed: dialogLoader.active = false
            }
        }

        onLoaded: item.open()
    }

}
