import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Rectangle {
    id: root
    color: "#798CA4"
    radius: 5

    readonly property int headerParts: 10
    readonly property int taskCol: 3
    readonly property int dateCol: 2
    readonly property int statusCol: 2
    readonly property int priorityCol: 2
    readonly property int typeCol: 1

    ColumnLayout {
        anchors.fill: parent

        // Actions Bar
        /*
        Item {
            id: actionsBar

            Layout.fillWidth: true
            Layout.preferredHeight: 50 // sortButton.implicitHeight

            Button {
                id: sortButton
                text: "Sort"
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                anchors.leftMargin: 10
            }

            RowLayout {
                anchors.centerIn: parent
                spacing: 5

                TextField {
                    id: searchField
                    Layout.preferredWidth: 200
                    Layout.preferredHeight: searchBtn.implicitHeight
                    placeholderText: "Search a Task..."
                    //onTextChanged: console.log("Texto actual:", text)
                }
                Button {
                    id: searchBtn
                    text: "Search"
                    onClicked: { }
                }
            }

            Button {
                id: newTaskButton
                text: "New Task"
                anchors.right: parent.right
                anchors.verticalCenter: parent.verticalCenter
                anchors.rightMargin: 10
                onClicked: { }
            }
        }

        // TABLE HEADER
        RowLayout {
            id: tableHeader
            Layout.fillWidth: true
            Layout.leftMargin: 10
            Layout.preferredHeight: 30
            Layout.alignment: Qt.AlignVCenter

            Text {
                id: taskText
                text: "TASK"
                font.bold: true
                Layout.preferredWidth: root.width * root.taskCol / root.headerParts
            }
            Text {
                text: "END DATE"
                font.bold: true
                Layout.preferredWidth: root.width * root.dateCol / root.headerParts
                Layout.alignment: Qt.AlignHCenter
            }
            Text {
                text: "STATUS"
                font.bold: true
                Layout.preferredWidth: root.width * root.statusCol / root.headerParts
                Layout.alignment: Qt.AlignHCenter
            }
            Text {
                text: "PRIORITY"
                font.bold: true
                Layout.preferredWidth: root.width * root.priorityCol / root.headerParts
                Layout.alignment: Qt.AlignHCenter
            }
            Text {
                text: "TYPE"
                font.bold: true
                Layout.preferredWidth: root.width * root.typeCol / root.headerParts
                Layout.alignment: Qt.AlignHCenter
            }
        }
        */

        ScrollView {
            id: scrollView

            Layout.fillWidth: true
            Layout.fillHeight: true

            ScrollBar.horizontal.interactive: false
            ScrollBar.vertical.interactive: true
            ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
            ScrollBar.vertical.policy: ScrollBar.AlwaysOn

            ColumnLayout {
                id: scrollColumn
                width: scrollView.availableWidth   // 👈 ancho fijo, SIN anchors.fill

                spacing: 250

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
