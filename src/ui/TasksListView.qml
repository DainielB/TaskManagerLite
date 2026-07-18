import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Rectangle {
    id: root
    color: "#798CA4"
    radius: 5

    ColumnLayout {
        anchors.fill: parent

        // Actions Bar
        Item {
            id: actionsBar
            Layout.fillWidth: true
            Layout.preferredHeight: sortButton.implicitHeight
            Layout.margins: 10

            Button {
                id: sortButton
                text: "Sort"
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
            }

            RowLayout {
                anchors.centerIn: parent
                spacing: 5

                TextField {
                    id: searchField
                    Layout.preferredWidth: 200
                    Layout.preferredHeight: searchBtn.implicitHeight
                    placeholderText: "Search a Task..."
                    onTextChanged: console.log("Texto actual:", text)
                }
                Button {
                    id: searchBtn
                    text: "Search"
                    onClicked: { /* tu lógica */ }
                }
            }

            Button {
                id: newTaskButton
                text: "New Task"
                anchors.right: parent.right
                anchors.verticalCenter: parent.verticalCenter
                onClicked: { /* tu lógica */ }
            }
        }

        Expandable {
            id: expandable
            Layout.fillWidth: true
            Layout.fillHeight: true

            headerText: "In Progress"
        }
    }
}
