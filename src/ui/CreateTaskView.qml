import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Dialog {
    property alias name: nameField.text
    property alias description: descriptionField.text
    property alias endDate: dateField.new_date
    property alias status: statusField
    property alias kind: kindField
    property alias priority: priorityField

    property bool is_modal
    property bool formValid: nameField.acceptableInput && kindField.currentIndex !== 0

    id: root
    width: Overlay.overlay.width / 4
    height: Overlay.overlay.height / 2
    title: qsTr("Create Task")
    visible: true
    modal: true
    closePolicy: Popup.CloseOnEscape
    anchors.centerIn: Overlay.overlay

    background: Rectangle {
        color: "#30332E"
//        border.color: "#4a4a5e"
//        border.width: 1
    }

    header: Rectangle {
        color: "#30332E"
        height: 36
        radius: 12
        Text {
            anchors.centerIn: parent
            text: root.title
            color: "white"
            font.pixelSize: 16
            font.bold: true
            wrapMode: Text.WordWrap
        }
    }

    contentItem: ColumnLayout {
        Layout.fillWidth: true
        Layout.fillHeight: true
        Layout.margins: 10
        spacing: 10

        TextField {
            id: nameField

            Layout.fillWidth: true
            Layout.fillHeight: false
            placeholderText: "Task Name"
            focus: true
            validator: input_validator
            background: Rectangle {
                radius: 4
                border.color: nameField.acceptableInput ? "transparent" : "red"
                border.width: nameField.acceptableInput ? 1 : 2
            }
        }

        TextArea {
            id: descriptionField
            Layout.fillWidth: true
            Layout.fillHeight: true
            placeholderText: "Task Description (Optional)"
            background: Rectangle {
                color: "white"
                radius: 4
                border.color: nameField.enabled ? "#21be2b" : "transparent"
            }
        }

        GridLayout {
            id: grid
            columns: 2
            rowSpacing: 10
            columnSpacing: 10

            Layout.fillWidth: true
            Layout.fillHeight: false

            DateInputView {
                id: dateField
                Layout.fillWidth: true
                Layout.preferredWidth: (grid.width - grid.columnSpacing) / 2
                is_enabled: true
                // date_validator: date_validator
            }

            ComboBox {
                id: statusField
                Layout.fillWidth: true
                Layout.preferredWidth: (grid.width - grid.columnSpacing) / 2
                enabled: true

                background: Rectangle {
                    color: "white"
                    radius: 4
                    border.color: nameField.enabled ? "#21be2b" : "transparent"
                }

                model: [
                    "Initial Status", "To Do", "In Progress", "In Review", "Paused", "Backlog"
                ]

                currentIndex: 0
            }

            ComboBox {
                id: kindField
                Layout.fillWidth: true
                Layout.preferredWidth: (grid.width - grid.columnSpacing) / 2
                enabled: true
                background: Rectangle {
                    color: "white"
                    radius: 4
                    border.color: nameField.enabled ? "#21be2b" : "transparent"
                }

                model: [
                    "Task Type", "Modeling", "Shading", "Rig", "Layout", "Animation", "FX", "Lighting", "Compositing"
                ]

                currentIndex: 0
            }

            /*
            ComboBox {
                id: priorityField
                Layout.fillWidth: true
                Layout.preferredWidth: (grid.width - grid.columnSpacing) / 2
                enabled: true
                background: Rectangle {
                    color: "white"
                    radius: 4
                    border.color: nameField.enabled ? "#21be2b" : "transparent"
                }

                model: [
                    "Priority", "Low", "Medium", "High", "Urgent"
                ]

                currentIndex: 0
            }
            */

            ComboBox {
                id: priorityField
                Layout.fillWidth: true
                enabled: true
                background: Rectangle {
                    color: "white"
                    radius: 4
                    border.color: nameField.enabled ? "#21be2b" : "transparent"
                }

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

    footer: DialogButtonBox {
        background: Rectangle { color: "transparent" }

        Button {
            text: "Cancel"
            flat: false
            DialogButtonBox.buttonRole: DialogButtonBox.RejectRole
            contentItem: Text { text: parent.text; color: "#aaaaaa" }
            background: Rectangle { color: "transparent" }
        }

        Button {
            text: "Accept"
            DialogButtonBox.buttonRole: DialogButtonBox.AcceptRole
            contentItem: Text { text: parent.text; color: "white"; font.bold: true }
            enabled: root.formValid
            background: Rectangle {
                color: enabled || parent.pressed ? "#637792" : "#7286A0"
                radius: 4
            }
        }
    }
}
