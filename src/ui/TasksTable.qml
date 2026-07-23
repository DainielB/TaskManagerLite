import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Rectangle {
    property int component_height: 36
    property int new_spacing: 15

    id: root

    color: "yellow"
    // implicitWidth: 50
    implicitHeight: 20

    /*
    ColumnLayout {
        anchors.fill: parent
        spacing: new_spacing

        ListView {
            id: listView
            Layout.fillWidth: true
            Layout.fillHeight: true
            clip: true

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
                        spacing: 30

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
    */

}
