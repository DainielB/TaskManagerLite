import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Rectangle {
    id: root

    property alias projectList: listView

    color: "#30332E"
    radius: 4

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

            Connections {
                target: listView.model

                function onRowsRemoved() {
                    Qt.callLater(function() {
                        listView.currentIndex = listView.count > 0 ? 0 : -1
                    })
                }

                function onRowsInserted(parent, first, last) {
                    Qt.callLater(function() {
                        listView.currentIndex = last
                        listView.positionViewAtIndex(last, ListView.Contain)
                    })
                }
            }

            Connections {
                target: app_controller.project_list_controller
                function onOnProjectSelection(projectId) {
                    app_controller.task_table_controller.task_table_model.refresh_table(projectId)
                }
            }

            Component {
                id: projectDelegate

                Item {
                    id: projectItem
                    width: listView.width
                    height: 48
                    // enabled: false

                    Text {
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: 10
                        text: name
                        color: projectItem.ListView.isCurrentItem ? "#F8D64F" : "white"
                    }

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onClicked: (mouse)=> {
                            listView.currentIndex = index
                            app_controller.project_list_controller.select_project(listView.currentIndex)

                            if (mouse.button == Qt.RightButton) {
                                context_menu.open()
                            }

                        }
                    }

                    Menu {
                        id: context_menu
                        x: (projectItem.width * 0.5)
                        y: (projectItem.height * 0.75)

                        MenuItem {
                            text: "Delete"
                            onReleased: {
                                app_controller.project_list_controller.remove_project(app_controller.project_list_controller.selected_project_id)
                            }
                        }
                        /*
                        MenuItem {
                            text: "Info"
                            onReleased: {
                                // TODO: Get current project information
                            }
                        }
                        */
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
