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

        ScrollView {
            id: scrollView
            //contentWidth: root.width
            //contentHeight: root.height
            Layout.fillWidth: true
            Layout.fillHeight: true

            ScrollBar.horizontal.interactive: false
            ScrollBar.vertical.interactive: true
            ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
            ScrollBar.vertical.policy: ScrollBar.AlwaysOn

            ColumnLayout {
                id: scrollColumn
                width: scrollView.availableWidth   // 👈 ancho fijo, SIN anchors.fill
                //anchors.fill: root

                spacing: 400

                Expandable {
                    id: inProgress

                    new_width: root.width
                    expanded: true
                    headerText: "In Progress"
                }

                Expandable {
                    id: inReview

                    new_width: root.width
                    expanded: false
                    headerText: "In Review"
                }

                Expandable {
                    id: toDo

                    new_width: root.width
                    expanded: false
                    headerText: "To Do"
                }

                Expandable {
                    id: paused

                    new_width: root.width
                    expanded: false
                    headerText: "Paused"
                }

                Expandable {
                    id: backlog

                    new_width: root.width
                    expanded: false
                    headerText: "Backlog"
                }

                Expandable {
                    id: finished

                    new_width: root.width
                    expanded: false
                    headerText: "Finished"
                }

            }

        }

    }
}
