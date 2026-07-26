import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Dialog {
    property alias name: nameField.text
    property alias description: descriptionField.text
    property alias endDate: dateField
    property alias status: statusField
    property alias type: typeField
    property alias priority: priorityField

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
        //anchors.fill: Overlay.overlay
        Layout.fillWidth: true
        Layout.fillHeight: true
        Layout.margins: 10
        spacing: 10

        TextField {
            id: nameField

            property bool isValid: nameField.text.length > 0

            Layout.fillWidth: true
            Layout.fillHeight: false
            placeholderText: "Task Name"
            focus: true
            validator: validator
            background: Rectangle {
                radius: 4
                border.color: nameField.isValid ? "transparent" : "red"
                border.width: nameField.isValid ? 1 : 2
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

            /*
            ColumnLayout {
                Layout.fillWidth: true
                Layout.fillHeight: false
                // spacing: 50

                Label {
                    text: "End Date"
                    Layout.fillWidth: true
                    color: "white"
                }

                DateInputView {
                    id: dateField
                    Layout.fillWidth: true
                    enabled: true
                }
            }
            */

            DateInputView {
                id: dateField
                Layout.fillWidth: true
                Layout.preferredWidth: (grid.width - grid.columnSpacing) / 2
                enabled: true
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
                    "Initial Status", "To Do", "In Progress", "In Review", "Paused", "Backlog", "Finished"
                ]

                currentIndex: 0

                onCurrentIndexChanged: {
                    console.log("Índice:", currentIndex)
                    console.log("Valor:", currentValue)
                    console.log("Texto:", currentText)
                }
            }

            ComboBox {
                id: typeField
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

                onCurrentIndexChanged: {
                    console.log("Índice:", currentIndex)
                    console.log("Valor:", currentValue)
                    console.log("Texto:", currentText)
                }
            }

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

                onCurrentIndexChanged: {
                    console.log("Índice:", currentIndex)
                    console.log("Valor:", currentValue)
                    console.log("Texto:", currentText)
                }
            }

        }

    }

    footer: DialogButtonBox {
        background: Rectangle { color: "transparent" }

        Button {
            text: "Cancel"
            flat: true
            DialogButtonBox.buttonRole: DialogButtonBox.RejectRole
            contentItem: Text { text: parent.text; color: "#aaaaaa" }
            background: Rectangle { color: "transparent" }
        }

        Button {
            text: "Accept"
            DialogButtonBox.buttonRole: DialogButtonBox.AcceptRole
            contentItem: Text { text: parent.text; color: "white"; font.bold: true }
            enabled: nameField.isValid
            background: Rectangle {
                color: enabled || parent.pressed ? "#637792" : "#7286A0"
                radius: 4
            }
        }
    }

//    standardButtons: Dialog.Ok | Dialog.Cancel
//    onReleased: app_controller.project_list_controller()
//    onRejected: createProjectDialog.on_cancel()

}
