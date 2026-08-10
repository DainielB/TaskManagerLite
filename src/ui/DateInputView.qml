import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Universal

Item {

    property var selectedDate: new Date()
    readonly property alias dateText: dateInput.placeholderText

    id: root
    width: 200
    height: 50

    RowLayout {
        anchors.fill: parent

        ColumnLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true

            TextField {
                id: dateInput
                Layout.fillWidth: true
                placeholderText: selectedDate.getFullYear() + "-" + (selectedDate.getMonth() + 1) + "-" + (selectedDate.getDate() + 1)
                enabled: true
                background: Rectangle {
                    color: "white"
                    radius: 4
                    border.color: nameField.enabled ? "#21be2b" : "transparent"
                }

                onTextEdited: dateInput.text = ""

                onReleased: datePicker.open()

                // validator: date_validator
            }
        }
    }

    Popup {
        id: datePicker
        width: dateInput.width
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside

        // Below the TextField
        x: dateInput.x
        y: dateInput.y + dateInput.height + (dateInput.height / 2)

        padding: 0

        contentItem: ColumnLayout {
            id: calendarLayout
            width: datePicker.width

            // Popup background
            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "white"
                border.color: "#cccccc"
                radius: 4
            }

            MonthGrid {
                id: grid
                month: root.selectedDate.getMonth()
                year: root.selectedDate.getFullYear()
                locale: Qt.locale("es_ES")
                Layout.fillWidth: true

                delegate: Text {
                    id: dateDelegateText
                    text: model.day + 1
                    opacity: model.month === grid.month ? 1 : 0.3
                    font.bold: model.today
                    horizontalAlignment: Text.AlignHCenter
                    color: model.date.getTime() === root.selectedDate.getTime()
                           ? "blue" : "orange"

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            root.selectedDate = model.date
                            dateInput.placeholderText = (model.date.getDate() + 1) + "/" +
                                (model.date.getMonth() + 1) + "/" +
                                model.date.getFullYear()
                            datePicker.close()
                        }
                    }
                }
            }

            // BOTTOM
            RowLayout {
                Layout.fillWidth: true

                Button {
                    Layout.fillWidth: true
                    text: "◄"
                    onClicked: {
                        if (grid.month === 0) {
                            grid.month = 11
                            grid.year -= 1
                        } else {
                            grid.month -= 1
                        }
                    }
                }

                Label {
                    Layout.fillWidth: true
                    horizontalAlignment: Text.AlignHCenter
                    text: Qt.locale("es_ES").monthName(grid.month)
                }

                Label {
                    Layout.fillWidth: true
                    horizontalAlignment: Text.AlignHCenter
                    text: grid.year
                }

                Button {
                    Layout.fillWidth: true
                    text: "►"
                    onClicked: {
                        if (grid.month === 11) {
                            grid.month = 0
                            grid.year += 1
                        } else {
                            grid.month += 1
                        }
                    }
                }
            }
        }
    }
}
