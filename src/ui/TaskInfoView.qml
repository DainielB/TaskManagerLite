import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Rectangle {
    id: root
    radius: 8
    // border.color: "#F0803C"
    color: "#9EACBD"

    property string name: "Name of the task"
    property string description: "Description of the task"
    property string endDate: ""
    property string status: ""
    property string type: ""
    property bool _enabled: false
    property bool _hasSelectedTask: false

    function enableButtons(enabled: bool) {
        cancelTask.enabled = enabled
        taskName.enabled = enabled
        taskDescription.enabled = enabled
        startDate.enabled = enabled
        dateInputView.enabled = enabled
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
            enabled: root._enabled
        }

        TextArea {
            id: taskDescription
            Layout.fillWidth: true
            Layout.fillHeight: true
            placeholderText: description
            enabled: root._enabled
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
                    id: dateInputView
                    Layout.fillWidth: true
                    Layout.fillHeight: false
                    // Layout.preferredWidth: (grid.width - grid.columnSpacing) / 2
                    is_enabled: root._enabled
                    // date_validator: date_validator
                }

            }

            ColumnLayout {
                spacing: 5

                Label {
                    text: "Status"
                }

                ComboBox {
                    id: taskStatus
                    Layout.fillWidth: true
                    enabled: root._enabled

                    model: [
                        "To Do", "In Progress", "In Review", "Paused", "Backlog", "Finished"
                    ]
                    currentIndex: 0

                    onCurrentIndexChanged: {

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
                    enabled: root._enabled

                    model: [
                        "Modeling", "Shading", "Rig", "Layout", "Animation", "FX", "Lighting", "Compositing"
                    ]
                    currentIndex: 0

                    onCurrentIndexChanged: {

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
                    enabled: root._enabled

                    /*
                    model: [
                        "Low", "Medium", "High", "Urgent"
                    ]
                    currentIndex: 0

                    onCurrentIndexChanged: {

                    }
                    */

                    model: [
                        {value: 1, text: "Low"},
                        {value: 2, text: "Medium"},
                        {value: 3, text: "High"},
                        {value: 4, text: "Urgent"}
                    ]
                    textRole: "text"
                    valueRole: "value"
                    currentIndex: 0
                }
            }

        }

        // Buttons Panel
        RowLayout {
            Layout.fillWidth: true
            spacing: 5

            Button {
                id: startTask
                text: "Start"
                visible: app_controller.task_info_controller.taskSelected
                onReleased: {
                    app_controller.task_info_controller.start_task()
                }
            }

            Item {
                Layout.fillWidth: true
            }

            Button {
                id: cancelTask
                text: "Cancel"
                enabled: root._enabled
                onReleased: root._enabled = !root._enabled
            }

            Button {
                id: editTask
                text: "Edit"
                enabled: true
                visible: !root._enabled
                onReleased: {
                   root._enabled = !root._enabled
                }
            }

            Button {
                id: saveTask
                text: "Save"
                enabled: root._enabled
                visible: root._enabled
                onReleased: {
                    app_controller.task_info_controller.save_task(taskName.text, taskDescription.text, dateInputView.new_date, taskStatus.currentValue, taskType.currentValue, priority.currentValue)
                    root._enabled = !root._enabled
                }
            }
        }
    }

    Connections {
        target: app_controller.task_info_controller

        function onTaskClicked(obj) {
            root._hasSelectedTask = true

            taskName.text = obj["NAME"]
            taskDescription.text = obj["DESCRIPTION"]
            dateInputView.new_date = obj["END_DATE"]
            taskStatus.currentValue = obj["STATUS"]
            taskType.currentValue = obj["KIND"]
            priority.currentValue = obj["PRIORITY"]
        }
    }

}
