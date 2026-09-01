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

    property var selectedTask: {}

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
                    enabled: root._enabled // false

                    model: [
                        "To Do", "In Progress", "In Review", "Paused", "Backlog", "Finished"
                    ]
                    currentIndex: 0

                    onCurrentIndexChanged: {
                    /*
                        console.log("Índice:", currentIndex)
                        console.log("Valor:", currentValue)
                        console.log("Texto:", currentText)
                    */
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
                onReleased: root._enabled = !root._enabled
            }

            Button {
                id: editTask
                text: "Edit"
                enabled: true
                visible: !root._enabled
                onReleased: {
                    // console.log("root.proxyModel FROM QML: ", root.proxyModel)
                    // root.proxyModel.get_task_index("TESTINGGG") // May be here I can get the index and then pass it as a reference to load_task()
                    // app_controller.task_info_controller.save_task(taskName.text, taskDescription.text, dateInputView.new_date, taskStatus.currentValue, taskType.currentValue, priority.currentValue)
                    root._enabled = !root._enabled // root.enableButtons(true)
                }
            }

            Button {
                id: saveTask
                text: "Save"
                enabled: root._enabled
                visible: root._enabled
                onReleased: {
                    // console.log("root.proxyModel FROM QML: ", root.proxyModel)
                    // root.proxyModel.get_task_index("TESTINGGG") // May be here I can get the index and then pass it as a reference to load_task()
                    app_controller.task_info_controller.save_task(taskName.text, taskDescription.text, dateInputView.new_date, taskStatus.currentValue, taskType.currentValue, priority.currentValue)
                    root._enabled = !root._enabled
                }
            }
        }
    }

    Connections {
        target: app_controller.task_info_controller

        function onTaskClicked(obj) {
            taskName.text = obj["NAME"]
            taskDescription.text = obj["DESCRIPTION"]
            dateInputView.new_date = obj["END_DATE"] // TODO: Find a way of setting the new date in the endDate textfield
            taskStatus.currentValue = obj["STATUS"]
            taskType.currentValue = obj["KIND"]
            priority.currentValue = obj["PRIORITY"]
        }
    }

}
