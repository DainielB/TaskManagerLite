import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Rectangle {
    id: taskList
    // property string projectName: ""

    color: "magenta"
    radius: 5
    border.color: "#dddddd"

    ColumnLayout {
        spacing: 8

        RowLayout {
            spacing: 8

            // Table actions item
            Item {
                Layout.fillWidth: true

                RowLayout {
                    spacing: 8

                    Button {
                        Layout.fillWidth: true
                        text: "Sort"
                    }

                }
            }

            Button {
                text: "New Task"
            }

        }
    }

    ListView {
        id: listView
        Layout.fillWidth: true
        Layout.fillHeight: true
        clip: true
        spacing: 2

        ScrollBar.vertical: ScrollBar {}

        model: ListModel {
            ListElement { nombre: "Tarea 1" }
            ListElement { nombre: "Tarea 2" }
            ListElement { nombre: "Tarea 3" }
        }

        delegate: Rectangle {
            width: lista.width
            height: 48
            color: ListView.isCurrentItem ? "#d0e8ff" : "white"   // resalta el seleccionado

            Text {
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.leftMargin: 10
                text: nombre
            }

            MouseArea {
                anchors.fill: parent
                onClicked: lista.currentIndex = index    // selecciona al hacer clic
            }
        }
    }

}
