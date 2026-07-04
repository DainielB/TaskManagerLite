import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Universal


Rectangle {
    Universal.theme: Universal.Light

    id: projectsList
    property string name: "Name of the task"
    property string description: "Description of the task"
    property string endDate: ""
    property string state: ""
    property string type: ""

    radius: 8
    border.color: "#dddddd"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 5

        TextField {
            id: taskName
            Layout.margins: 10
            Layout.fillWidth: true
            Layout.fillHeight: false
            text: name
            enabled: false
        }

        TextField {
            id: taskDescription
            Layout.margins: 10
            Layout.fillWidth: true
            Layout.fillHeight: true
            text: description
            enabled: false
        }

        // Task Info Panel
        GridLayout {
            columns: 2
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.margins: 10

            ColumnLayout {
                spacing: 5

                Label {
                    text: "Start Date"
                }

                TextField {
                    id: startDate
                    Layout.fillWidth: true
                    // Layout.fillHeight: true
                    enabled: false
                    text: "02-06-26"
                }
            }

            ColumnLayout {
                spacing: 5

                Label {
                    text: "End Date"
                }

                TextField {
                    id: endDate
                    Layout.fillWidth: true
                    // Layout.fillHeight: true
                    enabled: false
                    text: "28-06-26"
                }

            }

            ColumnLayout {
                spacing: 5

                Label {
                    text: "Status"
                }

                TextField {
                    id: taskStatus
                    Layout.fillWidth: true
                    // Layout.fillHeight: true
                    enabled: false
                    text: "In Progress"
                }
            }

            ColumnLayout {
                spacing: 5

                Label {
                    text: "Priority"
                }

                TextField {
                    id: priority
                    Layout.fillWidth: true
                    // Layout.fillHeight: true
                    enabled: false
                    text: "High"
                }
            }

        }

        // Buttons Panel
        RowLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.margins: 10
            Layout.alignment: Qt.AlignRight
            spacing: 5

            /*
            Button {
                text: "Edit"
            }

            Button {
                text: "Cancel"
            }
            */

            Button {
                id: editTask
                text: "Edit"
                onReleased: taskInfo.edit_button_released(editTask, [taskName, taskDescription, startDate, endDate, taskStatus, priority])
            }
        }
    }
}
