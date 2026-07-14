import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Universal


Dialog {
    property alias projectName: nameField
    property alias projectDescription: descriptionField
    property alias limitDateInput: dateField
    property alias projectColor: colorField

    id: createProject
    title: "Create Project"
    modal: true
    anchors.centerIn: parent
    width: parent.width / 4
    height: parent.height / 2
    closePolicy: Popup.CloseOnEscape

    ColumnLayout {
        anchors.fill: parent
        Layout.fillWidth: true
        Layout.fillHeight: true
        Layout.margins: 10
        spacing: 5

        TextField {
            id: nameField
            // Layout.margins: 10
            Layout.fillWidth: true
            Layout.fillHeight: false
            placeholderText: "Project Name"
            focus: true
        }

        TextField {
            id: descriptionField
            // Layout.margins: 10
            Layout.fillWidth: true
            Layout.fillHeight: true
            placeholderText: "Project Description (Optional)"
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
                }

                DateInputView {
                    id: dateField
                    Layout.fillWidth: true
                    enabled: true
                }
            }

            RowLayout {
                Layout.fillWidth: true
                Layout.fillHeight: false
                spacing: 50

                Label {
                    text: "Color (Optional)"
                    Layout.fillWidth: true
                }

                ComboBox {
                    id: colorField
                    Layout.fillWidth: true
                    enabled: true

                    model: [
                        "Lime", "Green", "Emerald", "Teal", "Cyan", "Cobalt", "Indigo", "Violet", "Purple", "Pink", "Magenta", "Crimson", "Red", "Orange",
                        "Amber", "Yellow", "Brown", "Olive", "Steel", "Mauve", "Taupe"
                    ]

                    /*
                    model: {
                        "Universal.Lime":"Lime", "Universal.Green":"Green", "Universal.Emerald":"Emerald", "Universal.Teal":"Teal", "Universal.Cyan":"Cyan", "Universal.Cobalt":"Cobalt",
                        "Universal.Indigo":"Indigo", "Universal.Violet":"Violet", "Universal.Purple":"Purple", "Universal.Pink":"Pink", "Universal.Magenta":"Magenta", "Universal.Crimson":"Crimson",
                        "Universal.Red":"Red", "Universal.Orange":"Orange", "Universal.Amber":"Amber", "Universal.Yellow":"Yellow", "Universal.Brown":"Brown", "Universal.Olive":"Olive",
                        "Universal.Steel":"Steel", "Universal.Mauve":"Mauve", "Universal.Taupe":"Taupe"
                    }
                    */

                    currentIndex: 0

                    onCurrentIndexChanged: {
                        console.log("Índice:", currentIndex)
                        console.log("Valor:", currentValue)
                        console.log("Texto:", currentText)
                    }
                }
            }
        }

    }

    standardButtons: Dialog.Ok | Dialog.Cancel

//    onRejected: createProjectDialog.on_cancel()

}
