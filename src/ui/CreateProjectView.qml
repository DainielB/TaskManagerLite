import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Dialog {
    property alias name: nameField.text
    property alias description: descriptionField.text
    property alias endDate: dateField.new_date
    // property alias projectColor: colorField

    id: createProject
    width: Overlay.overlay.width / 4
    height: Overlay.overlay.height / 2
    title: qsTr("Create Project")
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
        height: 48
        radius: 12
        Text {
            anchors.centerIn: parent
            text: createProject.title
            color: "white"
            font.pixelSize: 16
            font.bold: true
            wrapMode: Text.WordWrap
        }
    }

    contentItem: ColumnLayout {
        // anchors.fill: Overlay.overlay
        Layout.fillWidth: true
        Layout.fillHeight: true
        Layout.margins: 10
        spacing: 5

        TextField {
            id: nameField

            property bool isValid: nameField.text.length > 0

            Layout.fillWidth: true
            Layout.fillHeight: false
            placeholderText: "Project Name"
            focus: true
            background: Rectangle {
                //color: "white"
                radius: 4
                color: nameField.isValid ? "#4a4a5e" : "#e05252"
                border.width: !nameField.isValid ? 4 : 2
            }
        }

        TextArea {
            id: descriptionField
            Layout.fillWidth: true
            Layout.fillHeight: true
            placeholderText: "Project Description (Optional)"
            background: Rectangle {
                color: "white"
                radius: 4
                border.color: nameField.enabled ? "#21be2b" : "transparent"
            }
        }

        ColumnLayout {
            Layout.fillWidth: true
            Layout.fillHeight: false

            RowLayout {
                Layout.fillWidth: true
                Layout.fillHeight: false
                spacing: 50

                Label {
                    text: "Limit Date"
                    Layout.fillWidth: true
                    color: "white"
                }

                DateInputView {
                    id: dateField
                    Layout.fillWidth: true
                    enabled: true
                }
            }

            /*
            RowLayout {
                Layout.fillWidth: true
                Layout.fillHeight: false
                spacing: 50

                Label {
                    text: "Color (Optional)"
                    Layout.fillWidth: true
                    color: "white"
                }

                ComboBox {
                    id: colorField
                    Layout.fillWidth: true
                    enabled: true
                    background: Rectangle {
                        color: "white"
                        radius: 4
                        border.color: nameField.enabled ? "#21be2b" : "transparent"
                    }

                    model: [
                        "Lime", "Green", "Emerald", "Teal", "Cyan", "Cobalt", "Indigo", "Violet", "Purple", "Pink", "Magenta", "Crimson", "Red", "Orange",
                        "Amber", "Yellow", "Brown", "Olive", "Steel", "Mauve", "Taupe"
                    ]

                    model: {
                        "Universal.Lime":"Lime", "Universal.Green":"Green", "Universal.Emerald":"Emerald", "Universal.Teal":"Teal", "Universal.Cyan":"Cyan", "Universal.Cobalt":"Cobalt",
                        "Universal.Indigo":"Indigo", "Universal.Violet":"Violet", "Universal.Purple":"Purple", "Universal.Pink":"Pink", "Universal.Magenta":"Magenta", "Universal.Crimson":"Crimson",
                        "Universal.Red":"Red", "Universal.Orange":"Orange", "Universal.Amber":"Amber", "Universal.Yellow":"Yellow", "Universal.Brown":"Brown", "Universal.Olive":"Olive",
                        "Universal.Steel":"Steel", "Universal.Mauve":"Mauve", "º.Taupe":"Taupe"
                    }

                    currentIndex: 0

                    onCurrentIndexChanged: {
                        console.log("Índice:", currentIndex)
                        console.log("Valor:", currentValue)
                        console.log("Texto:", currentText)
                    }
                }
            }
            */
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
