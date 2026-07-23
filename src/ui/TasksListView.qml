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

            // contentHeight: scrollColumn.implicitHeight + 100 // TODO: modify this
            Component.onCompleted: console.log("scrollview width real:", scrollView.width, "implicitWidth:", implicitWidth, "scrollview height real:", scrollView.height, "implicitHeight:", implicitHeight)

            Layout.fillWidth: true
            Layout.fillHeight: true

            ScrollBar.horizontal.interactive: false
            ScrollBar.vertical.interactive: true
            ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
            ScrollBar.vertical.policy: ScrollBar.AlwaysOn

            /*
            background: Rectangle {
                color: "orange"
            }
            */

            ColumnLayout {
                id: scrollColumn
                width: scrollView.availableWidth   // 👈 ancho fijo, SIN anchors.fill

                // spacing: 20

                Expandable {
                    id: inProgress

                    Layout.alignment: Qt.AlignTop

                    implicitWidth: scrollView.width
                    implicitHeight: 200

                    header_height: 50
                    header_color: "blue"
                    expanded: true
                    headerText: "In Progress"
                }

                Expandable {
                    id: inReview

                    implicitWidth: scrollView.width
                    implicitHeight: 200

                    header_height: 50
                    header_color: "pink"
                    expanded: false
                    headerText: "In Review"
                }
                // Component.onCompleted: console.log("inReview width real:", inReview.width, "implicitWidth:", inReview.implicitWidth, "inReview height real:", inReview.height, "implicitHeight:", inReview.implicitHeight)

                Expandable {
                    id: toDo

                    implicitWidth: scrollView.width
                    implicitHeight: 200

                    header_height: 50
                    header_color: "purple"
                    expanded: false
                    headerText: "To Do"
                }

                Expandable {
                    id: paused

                    implicitWidth: scrollView.width
                    implicitHeight: 200

                    header_height: 50
                    header_color: "red"
                    expanded: false
                    headerText: "Paused"
                }

                Expandable {
                    id: backlog

                    implicitWidth: scrollView.width
                    implicitHeight: 200

                    header_height: 50
                    header_color: "green"
                    expanded: false
                    headerText: "Backlog"
                }

                Expandable {
                    id: finished

                    implicitWidth: scrollView.width
                    implicitHeight: 200

                    header_height: 50
                    header_color: "magenta"
                    expanded: false
                    headerText: "Finished"
                }

            }

        }

    }
}
