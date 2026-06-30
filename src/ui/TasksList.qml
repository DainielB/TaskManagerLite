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
        anchors.fill: parent
        spacing: 8

        GridLayout {
            /*
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignHCenter
            Layout.margins: 5
            spacing: 8
            */

            Layout.fillWidth: true
            Layout.margins: 20
            columns: 10
            Layout.alignment: Qt.AlignHCenter
            Layout.topMargin: 10

            // Table actions item
            Item {
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignLeft

                RowLayout {
                    spacing: 8

                    Button {
                        Layout.fillWidth: true
                        text: "Sort"
                    }

                }
            }

            // Search Bar
            RowLayout {

                TextField {
                    id: searchField
                    Layout.alignment: Qt.AlignVCenter
                    placeholderText: "Search a Task..."
                    onTextChanged: {
                        console.log("Texto actual:", text)
                    }
                }

                Button {
                    id: searchBtn
                    Layout.alignment: Qt.AlignVCenter
                    text: "Search"
                    enabled: true
                    highlighted: false
                    onClicked: {
                        // tu lógica
                    }
                }

            }

            Button {
                Layout.alignment: Qt.AlignRight
                text: "New Task"
            }

        }
    }

    ListView {
        id: listView
        Layout.alignment: Qt.AlignHCenter
        Layout.fillWidth: true
        Layout.fillHeight: true
        clip: true
        spacing: 2

        ScrollBar.vertical: ScrollBar {}

        model: ListModel {
            ListElement {
                name: "Bill Smith"
                number: "555 3264"
            }
            ListElement {
                name: "John Brown"
                number: "555 8426"
            }
            ListElement {
                name: "Sam Wise"
                number: "555 0473"
            }
        }

        delegate: Rectangle {
            width: listView.width
            height: 48
            color: ListView.isCurrentItem ? "#d0e8ff" : "white"

            Text {
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.leftMargin: 10
                text: nombre
            }

            MouseArea {
                anchors.fill: parent
                onClicked: listView.currentIndex = index    // selecciona al hacer clic
            }
        }
    }

}
