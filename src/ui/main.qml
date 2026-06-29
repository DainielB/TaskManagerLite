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

        RowLayout {
            Layout.fillWidth: true
            Layout.margins: 20
            spacing: 100
            Layout.alignment: Qt.AlignHCenter

            RowLayout {
                Layout.fillWidth: true
                spacing: 2

                TextField {
                    id: searchField
                    Layout.alignment: Qt.AlignVCenter
                    placeholderText: "Search a Task..."
                    Layout.preferredWidth: 200
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

        RowLayout {
            Layout.alignment: Qt.AlignHCenter
            Layout.fillWidth: true
            Layout.fillHeight: true
            spacing: 15

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "yellow"

                ColumnLayout {
                    id: projects
                    Layout.alignment: Qt.AlignHCenter
                    spacing: 10
                    Layout.fillWidth: true
                    // Layout.fillHeight: true

                    Text {
                        text: "Project 1"
                        Layout.fillHeight: true
                    }

                    Text {
                        text: "Project 2"
                        Layout.fillHeight: true
                    }

                    Button {
                        id: newProjectBtn
                        // Layout.alignment: Qt.AlignVCenter
                        text: "+ New Project"
                        enabled: true
                        highlighted: false
                        onClicked: {
                            // tu lógica
                        }
                    }
                }
            }

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "red"

                ColumnLayout {
                    id: tasks
                    Layout.alignment: Qt.AlignHCenter
                    spacing: 10
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    Text {
                        text: "Task 1"
                    }

                    Text {
                        text: "Task 2"
                    }
                }
            }

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "green"

                ColumnLayout {
                    id: taskInfo
                    Layout.alignment: Qt.AlignHCenter
                    spacing: 10
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    Text {
                        text: "Task Info 1"
                    }
                }
            }

        }
    }
}
