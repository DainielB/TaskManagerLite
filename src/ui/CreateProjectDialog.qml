import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Universal


Dialog {
    property var selectedDate: new Date()

    Universal.theme: Universal.Light

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
            id: projectName
            // Layout.margins: 10
            Layout.fillWidth: true
            Layout.fillHeight: false
            placeholderText: "Project Name"
        }

        TextField {
            id: projectDescription
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

                DateInput {
                    id: limitDateInput
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
                    id: projectColor
                    Layout.fillWidth: true
                    enabled: true

                    model: [
                        "Universal.Lime", "Universal.Green", "Universal.Emerald", "Universal.Teal", "Universal.Cyan", "Universal.Cobalt", "Universal.Indigo", "Universal.Violet",
                        "Universal.Purple", "Universal.Pink", "Universal.Magenta", "Universal.Crimson", "Universal.Red", "Universal.Orange", "Universal.Amber", "Universal.Yellow",
                        "Universal.Brown", "Universal.Olive", "Universal.Steel", "Universal.Mauve", "Universal.Taupe"
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

    }

    standardButtons: Dialog.Ok | Dialog.Cancel

    // onAccepted: console.log("Pulsado OK")
    // onRejected: console.log("Pulsado Cancelar")
}
