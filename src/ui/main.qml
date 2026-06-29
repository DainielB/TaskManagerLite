import QtQuick.Window
import QtQuick.Layouts
import QtQuick.Controls


Window {
    id: mainWindow

    width: 800
    height: 600
    visible: true
    title: "Task Manager Lite"

    minimumWidth: 400
    minimumHeight: 300

    ColumnLayout {
        anchors.fill: parent
        spacing: 10

        RowLayout {
            Layout.alignment: Qt.AlignHCenter
            spacing: 10

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

        Item { Layout.fillHeight: true }

        RowLayout {
            Layout.alignment: Qt.AlignHCenter
            spacing: 10

            Rectangle {
                Layout.alignment: Qt.AlignVCenter
                id: projects
                color: "blue"
            }

            Rectangle {
                Layout.alignment: Qt.AlignVCenter
                id: tasks
                color: "green"
            }

            Rectangle {
                Layout.alignment: Qt.AlignVCenter
                id: taskInfo
                color: "yellow"
            }
        }
    }
}
