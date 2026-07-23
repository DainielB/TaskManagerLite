import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Rectangle {
    property int component_height: 36
    property int tasks_spacing: 5
    readonly property alias contentHeight: listView.contentHeight

    id: root
    color: "transparent"

    // Component.onCompleted: console.log("listView.contentHeight:", listView.contentHeight, "| count:", listView.count)

    ColumnLayout {
        anchors.fill: parent
        spacing: tasks_spacing

        ListView {
            id: listView
            Layout.fillWidth: true
            Layout.fillHeight: true
            clip: true
            spacing: tasks_spacing

            model: app_controller.task_table_controller.task_table_model

            Component {
                id: taskDelegate

                Rectangle {
                    width: listView.width
                    height: component_height
                    color: "#9EACBD"
                    radius: 5

                    border.width: 1
                    border.color: "gray"

                    RowLayout {
                        anchors.fill: parent
                        anchors.leftMargin: 10
                        // spacing: 30

                        Text {
                            text: name // TODO: Esto es lo que hace que cuando se cree un proyecto nuevo,
                                        // los que ya hay en la lista se actualicen automáticamente con el nombre
                                        // que se está poniendo en el textfield
                            color: listView.isCurrentItem ? "black" : "white"
                        }

                        Text {
                            text: end_date
                            color: listView.isCurrentItem ? "black" : "white"
                        }

                        Text {
                            text: status
                            color: listView.isCurrentItem ? "black" : "white"
                        }

                        Text {
                            text: priority
                            color: listView.isCurrentItem ? "black" : "white"
                        }

                        Text {
                            text: type
                            color: listView.isCurrentItem ? "black" : "white"
                        }

                    }

                    MouseArea {
                        anchors.fill: parent
                        onClicked: listView.currentIndex = index
                    }
                }
            }

            delegate: taskDelegate  // RowLayout con cada "columna" como componente distinto
        }
    }

}
