import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Rectangle {
    property int component_height: 36
    property int tasks_spacing: 5
    readonly property alias contentHeight: listView.contentHeight
    readonly property int headerParts: 10
    readonly property int taskCol: 3
    readonly property int dateCol: 2
    readonly property int statusCol: 2
    readonly property int priorityCol: 2
    readonly property int typeCol: 1

    property var proxyModel
    property string status: ""

    id: root
    color: "transparent"

    ColumnLayout {
        anchors.fill: parent
        spacing: tasks_spacing

        ListView {
            id: listView
            Layout.fillWidth: true
            Layout.fillHeight: true
            clip: true
            spacing: tasks_spacing

            model: root.proxyModel

            Component {
                id: taskDelegate

                Rectangle {
                    width: listView.width
                    height: component_height
                    color: "#9EACBD"
                    radius: 5

                    border.width: 2
                    border.color: "#F0803C"

                    RowLayout {
                        anchors.fill: parent
                        anchors.leftMargin: 10

                        Text {
                            text: model.name
                            color: listView.isCurrentItem ? "black" : "white"
                            Layout.preferredWidth: root.width * root.taskCol / root.headerParts
                        }

                        Text {
                            text: model.end_date
                            color: listView.isCurrentItem ? "black" : "white"
                            Layout.preferredWidth: root.width * root.dateCol / root.headerParts
                        }
                        Text {
                            text: model.priority
                            color: listView.isCurrentItem ? "black" : "white"
                            Layout.preferredWidth: root.width * root.priorityCol / root.headerParts
                        }

                        Text {
                            text: model.kind
                            color: listView.isCurrentItem ? "black" : "white"
                            Layout.preferredWidth: root.width * root.typeCol / root.headerParts
                        }

                    }

                    MouseArea {
                        anchors.fill: parent
                        onReleased: {
                            listView.currentIndex = index
                            app_controller.task_info_controller.load_task(model.id)
                        }
                    }
                }
            }

            delegate: taskDelegate
        }
    }

}
