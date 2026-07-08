import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Rectangle {
    id: taskList
    color: "magenta"
    radius: 5
    border.color: "#dddddd"

    ColumnLayout {
        anchors.fill: parent
        spacing: 0

        // Actions Bar
        RowLayout {
            Layout.fillWidth: true
            Layout.margins: 5
            spacing: 5

            Button {
                text: "Sort"
            }

            Item { Layout.fillWidth: true }

            TextField {
                id: searchField
                placeholderText: "Search a Task..."
                Layout.preferredWidth: 200
                Layout.preferredHeight: searchBtn.implicitHeight
                onTextChanged: console.log("Texto actual:", text)
            }
            Button {
                id: searchBtn
                text: "Search"
                onClicked: { /* tu lógica */ }
            }

            Item { Layout.fillWidth: true }

            Button {
                text: "New Task"
                onClicked: { /* tu lógica */ }
            }
        }

        // Tasks List
        ListView {
            id: listView
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.margins: 5
            clip: true
            spacing: 2

            ScrollBar.vertical: ScrollBar {}

            model: ListModel {
                ListElement { name: "Bill Smith";  number: "555 3264" }
                ListElement { name: "John Brown";  number: "555 8426" }
                ListElement { name: "Sam Wise";    number: "555 0473" }
            }

            delegate: Rectangle {
                width: listView.width
                height: 48
                color: ListView.isCurrentItem ? "#d0e8ff" : "white"

                Text {
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.left: parent.left
                    anchors.leftMargin: 10
                    text: name + ": " + number
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: listView.currentIndex = index
                }
            }
        }
    }
}
