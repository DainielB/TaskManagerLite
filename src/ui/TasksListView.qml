import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


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

    ColumnLayout {
        anchors.fill: parent

        // Actions Bar
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
                    Layout.preferredWidth: root.width * root.taskCol / root.headerParts
                    Layout.alignment: Qt.AlignHCenter
                    background: Rectangle {
                        color: "transparent"
                    }

                    Text {
                        id: taskText
                        text: "TASK"
                        font.bold: true
                    }

                    // hoverEnabled: true

                    onReleased: {
                        app_controller.task_table_controller.task_filter_proxy.set_sort_role("name", 0)
                    }

                }

                Button {
                    Layout.preferredWidth: root.width * root.dateCol / root.headerParts
                    Layout.alignment: Qt.AlignHCenter
                    background: Rectangle {
                        color: "transparent"
                    }

                    Text {
                        text: "END DATE"
                        font.bold: true
                    }

                    onReleased: {
                        app_controller.task_table_controller.task_filter_proxy.set_sort_role("end_date", 1)
                    }
                }

                Button {
                    Layout.preferredWidth: root.width * root.priorityCol / root.headerParts
                    Layout.alignment: Qt.AlignHCenter
                    background: Rectangle {
                        color: "transparent"
                    }

                    Text {
                        text: "PRIORITY"
                        font.bold: true
                    }

                    onReleased: {
                        app_controller.task_table_controller.task_filter_proxy.set_sort_role("priority", 2)
                    }
                }

                Button {
                    Layout.preferredWidth: root.width * root.typeCol / root.headerParts
                    Layout.alignment: Qt.AlignHCenter
                    background: Rectangle {
                        color: "transparent"
                    }

                    Text {
                        text: "TYPE"
                        font.bold: true
                    }

                    onReleased: {
                        app_controller.task_table_controller.task_filter_proxy.set_sort_role("kind", 3)
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
            ScrollBar.vertical.policy: ScrollBar.AlwaysOff // ScrollBar is not visible but works

            /*
            background: Rectangle {
                color: "orange"
            }
            */

            ColumnLayout {
                id: scrollColumn
                width: scrollView.availableWidth

                spacing: 15

                Expandable {
                    id: inProgress

                    proxyModel: app_controller.task_table_controller.in_progress_proxy

                    Layout.fillWidth: true

                    header_height: 50
                    header_color: "#30332E"
                    expanded: true
                    headerText: "In Progress"
                    status: "In Progress"
                }

                Expandable {
                    id: inReview

                    proxyModel: app_controller.task_table_controller.in_review_proxy

                    Layout.fillWidth: true

                    header_height: 50
                    header_color: "#30332E"
                    expanded: false
                    headerText: "In Review"
                    status: "In Review"
                }

                Expandable {
                    id: toDo

                    proxyModel: app_controller.task_table_controller.to_do_proxy

                    Layout.fillWidth: true

                    header_height: 50
                    header_color: "#30332E"
                    expanded: false
                    headerText: "To Do"
                    status: "To Do"
                }

                Expandable {
                    id: paused

                    proxyModel: app_controller.task_table_controller.paused_proxy

                    Layout.fillWidth: true

                    header_height: 50
                    header_color: "#30332E"
                    expanded: false
                    headerText: "Paused"
                    status: "Paused"
                }

                Expandable {
                    id: backlog

                    proxyModel: app_controller.task_table_controller.backlog_proxy

                    Layout.fillWidth: true

                    header_height: 50
                    header_color: "#30332E"
                    expanded: false
                    headerText: "Backlog"
                    status: "Backlog"
                }

                Expandable {
                    id: finished

                    proxyModel: app_controller.task_table_controller.finished_proxy

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
