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

        /*
        RowLayout {
            Layout.fillWidth: true
            Layout.margins: 20
            spacing: 100
            Layout.alignment: Qt.AlignHCenter
            Layout.topMargin: 10

            RowLayout {

                TextField {
                    id: searchField
                    Layout.alignment: Qt.AlignVCenter
                    placeholderText: "Search a Task..."
                    onTextChanged: {
                        console.log("Texto actual:", text)
                    }
                }

                Button {
                    id: searchBtn
                    Layout.alignment: Qt.AlignVCenter
                    text: "Search"
                    enabled: true
                    highlighted: false
                    onClicked: {
                        // tu lógica
                    }
                }

            }

            Button {
                id: newTaskBtn
                Layout.alignment: Qt.AlignVCenter
                text: "New Task"
                enabled: true
                highlighted: false
                onClicked: {
                    // tu lógica
                }
            }
        }
        */

        GridLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            columns: 10
            // columnSpacing: 5

            ProjectsList {
                id: projects
                projectName: "Project Test"
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.preferredWidth: 1
                // Layout.horizontalStretchFactor: 1
            }

            TasksList {
                id: tasksList
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.preferredWidth: 4
                // Layout.horizontalStretchFactor: 2
            }

            TaskInfo {
                id: tasks
                // color: "blue"
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.preferredWidth: 2
                // Layout.horizontalStretchFactor: 1
            }

        }

    }
}
