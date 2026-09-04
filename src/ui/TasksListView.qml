import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

import TaskProxyModel 1.0


Rectangle {
    id: root
    color: "#798CA4"
    radius: 5

    readonly property int headerParts: 14
    readonly property int taskCol: 3
    readonly property int dateCol: 2
    readonly property int statusCol: 2
    readonly property int priorityCol: 2
    readonly property int typeCol: 1

    property var allProxies: [inProgressProxy, inReviewProxy, toDoProxy, pausedProxy, backlogProxy, finishedProxy]
    property var allExpandables: [inProgress, inReview, toDo, paused, backlog, finished]

    function sortAllBy(role) {
        for (let i = 0; i < allProxies.length; i++) {
            allProxies[i].set_sort_role(role)
        }
    }

    function filterAllBy(text) {
        for (let i = 0; i < allProxies.length; i++) {
            allProxies[i].search_all_by(text)
        }
        for (let i = 0; i < allExpandables.length; i++) {
            allExpandables[i].expanded = true
        }
    }

    ColumnLayout {
        anchors.fill: parent

        // Actions Bar
        Item {
            id: actionsBar

            Layout.fillWidth: true
            Layout.preferredHeight: 50 // sortButton.implicitHeight

            /*
            Button {
                id: sortButton
                text: "Sort"
                anchors.left: parent.left
                anchors.verticalCenter: parent.verticalCenter
                anchors.leftMargin: 10
            }
            */

            RowLayout {
                anchors.centerIn: parent
                spacing: 5

                TextField {
                    id: searchField
                    Layout.preferredWidth: 200
                    Layout.preferredHeight: newTaskButton.implicitHeight
                    placeholderText: "Search a Task..."
                    onTextChanged: searchTimer.restart()
                }

                Timer {
                    id: searchTimer
                    interval: 250
                    onTriggered: root.filterAllBy(searchField.text)
                }

                /*
                Button {
                    id: searchBtn
                    text: "Search"
                    onClicked: { }
                }
                */
            }

            Button {
                id: newTaskButton
                text: "New Task"
                anchors.right: parent.right
                anchors.verticalCenter: parent.verticalCenter
                anchors.rightMargin: 10

                onReleased: createTaskLoader.active = true
            }
        }

        // TABLE HEADER
        Rectangle {
            id: tableHeaderBackground

            Layout.fillWidth: true
            Layout.preferredHeight: 30
            Layout.alignment: Qt.AlignVCenter

            color: "#9EACBD" // #798DA4

            RowLayout {
                id: tableHeader

                anchors.fill: parent
                anchors.verticalCenter: parent.verticalCenter

                Button {
                    Layout.fillWidth: false
                    Layout.fillHeight: true
                    Layout.alignment: Qt.AlignHCenter
                    Layout.preferredWidth: root.width * root.taskCol / root.headerParts
                    background: Rectangle {
                        color: "transparent"
                    }

                    Text {
                        id: taskText
                        text: "TASK"
                        font.bold: true
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.horizontalCenter: parent.horizontalCenter
                    }

                    // hoverEnabled: true

                    onReleased: {
                        root.sortAllBy("name")
                    }

                }

                Button {
                    Layout.fillHeight: true
                    Layout.preferredWidth: root.width * root.dateCol / root.headerParts
                    Layout.alignment: Qt.AlignHCenter
                    background: Rectangle {
                        color: "transparent"
                    }

                    Text {
                        text: "END DATE"
                        font.bold: true
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.horizontalCenter: parent.horizontalCenter
                    }

                    onReleased: {
                        root.sortAllBy("end_date")
                    }
                }

                Button {
                    Layout.fillHeight: true
                    Layout.preferredWidth: root.width * root.priorityCol / root.headerParts
                    Layout.alignment: Qt.AlignHCenter
                    background: Rectangle {
                        color: "transparent"
                    }

                    Text {
                        text: "PRIORITY"
                        font.bold: true
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.horizontalCenter: parent.horizontalCenter
                    }

                    onReleased: {
                        root.sortAllBy("priority")
                    }
                }

                Button {
                    Layout.fillHeight: true
                    Layout.preferredWidth: root.width * root.typeCol / root.headerParts
                    Layout.alignment: Qt.AlignHCenter
                    background: Rectangle {
                        color: "transparent"
                    }

                    Text {
                        text: "TYPE"
                        font.bold: true
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.horizontalCenter: parent.horizontalCenter
                    }

                    onReleased: {
                        root.sortAllBy("kind")
                    }
                }

            }

        }

        ScrollView {
            id: scrollView

            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.margins: 10

            ScrollBar.horizontal.interactive: false
            ScrollBar.vertical.interactive: true
            ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
            ScrollBar.vertical.policy: ScrollBar.AlwaysOff // ScrollBar is not visible but it works

            /*
            background: Rectangle {
                color: "orange"
            }
            */

            ColumnLayout {
                id: scrollColumn
                width: scrollView.availableWidth

                spacing: 15

                TaskSortFilterProxy {
                    id: inProgressProxy
                    source_model: app_controller.task_table_controller.task_table_model
                    status: "In Progress"
                }

                Expandable {
                    id: inProgress

                    proxyModel: inProgressProxy

                    Layout.fillWidth: true

                    header_height: 50
                    header_color: "#30332E"
                    expanded: true
                    headerText: "In Progress"
                    status: "In Progress"
                }

                TaskSortFilterProxy {
                    id: inReviewProxy
                    source_model: app_controller.task_table_controller.task_table_model
                    status: "In Review"
                }

                Expandable {
                    id: inReview

                    proxyModel: inReviewProxy

                    Layout.fillWidth: true

                    header_height: 50
                    header_color: "#30332E"
                    expanded: false
                    headerText: "In Review"
                    status: "In Review"
                }

                TaskSortFilterProxy {
                    id: toDoProxy
                    source_model: app_controller.task_table_controller.task_table_model
                    status: "To Do"
                }

                Expandable {
                    id: toDo

                    proxyModel: toDoProxy

                    Layout.fillWidth: true

                    header_height: 50
                    header_color: "#30332E"
                    expanded: false
                    headerText: "To Do"
                    status: "To Do"
                }

                TaskSortFilterProxy {
                    id: pausedProxy
                    source_model: app_controller.task_table_controller.task_table_model
                    status: "Paused"
                }

                Expandable {
                    id: paused

                    proxyModel: pausedProxy

                    Layout.fillWidth: true

                    header_height: 50
                    header_color: "#30332E"
                    expanded: false
                    headerText: "Paused"
                    status: "Paused"
                }

                TaskSortFilterProxy {
                    id: backlogProxy
                    source_model: app_controller.task_table_controller.task_table_model
                    status: "Backlog"
                }

                Expandable {
                    id: backlog

                    proxyModel: backlogProxy

                    Layout.fillWidth: true

                    header_height: 50
                    header_color: "#30332E"
                    expanded: false
                    headerText: "Backlog"
                    status: "Backlog"
                }

                TaskSortFilterProxy {
                    id: finishedProxy
                    source_model: app_controller.task_table_controller.task_table_model
                    status: "Finished"
                }

                Expandable {
                    id: finished

                    proxyModel: finishedProxy

                    Layout.fillWidth: true

                    header_height: 50
                    header_color: "#30332E"
                    expanded: false
                    headerText: "Finished"
                    status: "Finished"
                }

            }

        }

    }
}
