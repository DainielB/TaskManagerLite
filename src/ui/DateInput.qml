import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Universal


Item {
    property var selectedDate: new Date()

    width: 200
    height: 50

    RowLayout {
        anchors.fill: parent

        TextField {
            id: dateInput
            Layout.fillWidth: true
            placeholderText: selectedDate.getDate() + "/" + (selectedDate.getMonth() + 1) + "/" + selectedDate.getFullYear()
            onReleased: datePicker.visible = !datePicker.visible
        }

        /*
        Button {
            Layout.fillWidth: true
            text: "▼"
        }

        Rectangle {
            Layout.fillWidth: true
            height: 50
            visible: False
        }
        */

        Item {
            id: datePicker
            Layout.fillWidth: true
            height: 100
            width: dateInput.width
            y: dateInput.y + dateInput.height
            visible: false

            ColumnLayout {
                Layout.fillWidth: true

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

                RowLayout {
                    Layout.fillWidth: true

                    Button {
                        Layout.fillWidth: true
                        text: "◄"
                    }

                    Label {
                        Layout.fillWidth: true
                        text: "Month"
                    }

                    Label {
                        Layout.fillWidth: true
                        text: "Year"
                    }

                    Button {
                        Layout.fillWidth: true
                        text: "►"
                    }

                }

            }
        }

    }
}
