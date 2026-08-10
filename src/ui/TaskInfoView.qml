import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Rectangle {
    id: root
    radius: 8
    border.color: "#F0803C"
    color: "#9EACBD"

    property string name: "Name of the task"
    property string description: "Description of the task"
    property string endDate: ""
    property string status: ""
    property string type: ""
    property bool _enabled: false

    function enableButtons(enabled: bool) {
        cancelTask.enabled = enabled
        taskName.enabled = enabled
        taskDescription.enabled = enabled
        startDate.enabled = enabled
        endDate.enabled = enabled
        taskStatus.enabled = enabled
        priority.enabled = enabled
    }

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 10

        TextField {
            id: taskName
            Layout.fillWidth: true
            Layout.fillHeight: false
            placeholderText: name
            enabled: root._enabled // false
        }

        TextArea {
            id: taskDescription
            Layout.fillWidth: true
            Layout.fillHeight: true
            placeholderText: description
            enabled: root._enabled // false
        }

        // Task Info Panel
        GridLayout {
            columns: 2
            Layout.fillWidth: true
            Layout.fillHeight: true

            ColumnLayout {
                spacing: 5

                Label {
                    text: "End Date"
                }

                DateInputView {
                    id: endDate
                    Layout.fillWidth: true
                    Layout.fillHeight: false
                    // Layout.preferredWidth: (grid.width - grid.columnSpacing) / 2
                    is_enabled: root._enabled
                    // date_validator: date_validator
                }

                /*
                TextField {
                    id: endDate
                    Layout.fillWidth: true
                    Layout.fillHeight: false
                    enabled: root._enabled // false
                    text: "28-06-26"
                }
                */

            }

            ColumnLayout {
                spacing: 5

                Label {
                    text: "Status"
                }

                ComboBox {
                    id: taskStatus
                    Layout.fillWidth: true
                    enabled: root._enabled // false

                    model: [
                        "To Do", "In Progress", "In Review", "Paused", "Backlog", "Finished"
                    ]
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
                    text: "Task Type"
                }

                ComboBox {
                    id: taskType
                    Layout.fillWidth: true
                    enabled: root._enabled // false

                    model: [
                        "Modeling", "Shading", "Rig", "Layout", "Animation", "FX", "Lighting", "Compositing"
                    ]
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
                    Layout.fillWidth: true
                    enabled: root._enabled // false

                    model: [
                        "Low", "Medium", "High", "Urgent"
                    ]
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
            Layout.alignment: Qt.AlignRight
            spacing: 5

            Button {
                id: cancelTask
                text: "Cancel"
                enabled: root._enabled // false
                onReleased: taskInfo.cancel_button_released(editTask, cancelTask, [taskName, taskDescription, startDate, endDate, taskStatus, priority])
            }

            Button {
                id: editTask
                text: root._enabled ? "Save" : "Edit"
                enabled: true
                onReleased: root._enabled = !root._enabled // root.enableButtons(true)
            }
        }
    }

}
