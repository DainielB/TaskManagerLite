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
    // background: Universal.Yellow

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

        RowLayout {
            Layout.fillWidth: true
            Layout.fillHeight: false
            // spacing: 50

            /*
            ColumnLayout {
                // anchors.fill: parent
                Layout.fillWidth: true
                Layout.fillHeight: true

                DayOfWeekRow {
                    locale: Qt.locale("es_ES")
                    Layout.fillWidth: true
                }

                MonthGrid {
                    id: grid
                    month: selectedDate.getMonth()
                    year: selectedDate.getFullYear()
                    locale: Qt.locale("es_ES")
                    Layout.fillWidth: true

                    delegate: Text {
                        text: model.day
                        opacity: model.month === grid.month ? 1 : 0.3
                        font.bold: model.today
                        color: model.date.getTime() === createProject.selectedDate.getTime() ? "blue" : "orange"
                        // color: model.date.getTime() === createProject.selectedDate.getTime() ? "blue" : "black"

                        MouseArea {
                            anchors.fill: parent
                            onClicked: createProject.selectedDate = model.date
                        }
                    }
                }
            }
            */

            TextField {
                id: limitDate
                Layout.fillWidth: true
                enabled: true
                placeholderText: "28-06-26"
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

    standardButtons: Dialog.Ok | Dialog.Cancel

    onAccepted: console.log("Pulsado OK")
    onRejected: console.log("Pulsado Cancelar")
}
