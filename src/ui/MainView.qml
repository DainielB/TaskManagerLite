import QtQuick.Window
import QtQuick.Layouts
import QtQuick.Controls


Window {
    id: mainWindow

    color: "#2A1F2D"
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

            ProjectsListView {
                id: projectsListView
//                Layout.preferredWidth: 1
            }

            TasksListView {
                id: tasksList
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.preferredWidth: 4
            }

            TaskInfoView {
                id: tasks
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.preferredWidth: 2
            }

        }

    }

    CreateProjectView {
        id: projectDialog
        onAccepted: app_controller.project_list_controller.add_new_project(projectDialog.projectName, projectDialog.projectDescription, projectDialog.limitDateInput.dateInput, projectDialog.projectColor)
    }
}
