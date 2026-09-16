import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Rectangle {
    id: root

    property alias projectList: listView

    color: "#30332E"
    radius: 4
    // border.color: "#F8D64F"

    ColumnLayout {
        anchors.fill: parent

        ListView {
            id: listView
            Layout.alignment: Qt.AlignHCenter
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.margins: 5
            clip: true
            spacing: 50
            highlight: Rectangle { color: "#7286A0" }

            ScrollBar.vertical: ScrollBar {}

            model: app_controller.project_list_controller.project_list_model
            onCurrentIndexChanged: {
                /*
                if (currentIndex >= 0) {
                    app_controller.project_list_controller.select_project(currentIndex)
                }
                */
            }

            // TODO: Disabled project currenty selected
            Component {
                id: projectDelegate

                Item {
                    width: listView.width
                    height: 48

                    Text {
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: 10
                        text: name
                        color: listView.isCurrentItem ? "black" : "white"
                    }

                    MouseArea {
                        anchors.fill: parent
                        onClicked:{
                            listView.currentIndex = index
                            app_controller.project_list_controller.select_project(listView.currentIndex)
                            app_controller.task_table_controller.task_table_model.refresh_table(app_controller.project_list_controller.selected_project_id)
                        }
                    }
                }
            }

            delegate: projectDelegate
        }

        RowLayout {
            spacing: 10

            Item {
                Layout.alignment: Qt.AlignHCenter
                Layout.fillWidth: true
                Layout.fillHeight: true

                Button {
                    id: newProjectButton
                    background: Rectangle {
                        implicitWidth: 100
                        implicitHeight: 40
                        enabled: true
//                        opacity: enabled ? 1 : 0.3
                        color: "#F8D64F"
                    }
                    anchors.bottom: parent.bottom
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.bottomMargin: 20
                    enabled: true
                    highlighted: false
                    font.bold: true
                    width: 150
                    text: "+ New Project"

                    onReleased: createProjectLoader.active = true
                }
            }

        }

    }

}
