import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
// import QtQuick.Controls.Universal


Rectangle {
    // Universal.theme: Universal.Light

    id: projectsList
    property string name: "Name of the task"
    property string description: "Description of the task"
    property string endDate: ""
    property string state: ""
    property string type: ""

    radius: 8
    border.color: "#dddddd"

    ColumnLayout {
        Layout.fillWidth: true
        Layout.fillHeight: true
        Layout.margins: 10
        spacing: 5

        TextField {
            id: taskName
            /*
            Layout.fillWidth: true
            Layout.fillHeight: false
            */
            text: name
            enabled: false
        }

        TextField {
            id: taskDescription
            /*
            Layout.margins: 10
            Layout.fillWidth: true
            Layout.fillHeight: true
            */
            text: description
            enabled: false
        }

        // Task Info Panel
        GridLayout {
            columns: 2
            /*
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.margins: 10
            */

            ColumnLayout {
                spacing: 5

                Label {
                    text: "Start Date"
                }

                TextField {
                    id: startDate
                    /*
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    */
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
                    /*
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    */
                    enabled: false
                    text: "28-06-26"
                }

            }

            ColumnLayout {
                spacing: 5

                Label {
                    text: "Status"
                }

                ComboBox {
                    id: taskStatus
                    // Layout.fillWidth: true
                    enabled: false

                    model: ["In Progress", "In Review", "To Do", "Paused", "Backlog", "Finished"]
                    currentIndex: 0

                    onCurrentIndexChanged: {
                        console.log("Índice:", currentIndex)
                        console.log("Valor:", currentValue)
                        console.log("Texto:", currentText)
                    }
                }
            }

            ColumnLayout {
                spacing: 5

                Label {
                    text: "Priority"
                }

                ComboBox {
                    id: priority
                    // Layout.fillWidth: true
                    enabled: false

                    model: ["High", "Medium", "Low"]
                    currentIndex: 0

                    onCurrentIndexChanged: {
                        console.log("Índice:", currentIndex)
                        console.log("Valor:", currentValue)
                        console.log("Texto:", currentText)
                    }
                }
            }

        }

        // Buttons Panel
        RowLayout {
            /*
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.margins: 10
            */
            Layout.alignment: Qt.AlignRight
            spacing: 5

            /*
            Button {
                text: "Edit"
            }
            */

            Button {
                id: cancelTask
                text: "Cancel"
                enabled: false
                onReleased: taskInfo.cancel_button_released(editTask, cancelTask, [taskName, taskDescription, startDate, endDate, taskStatus, priority])
            }

            Button {
                id: editTask
                text: "Edit"
                onReleased: taskInfo.edit_button_released(editTask, [cancelTask, taskName, taskDescription, startDate, endDate, taskStatus, priority])
            }
        }
    }
}
