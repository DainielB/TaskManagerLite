import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Rectangle {
    id: root

    property alias projectList: listView

    color: "#30332E"
    radius: 4

    function load_projects() {
        app_controller.project_list_controller.select_project(listView.currentIndex)
        
        app_controller.task_table_controller.task_table_model.refresh_table(app_controller.project_list_controller.selected_project_id)
    }

    function reset_index(index) {
        if (index >= 1) {
            index -= 1
            // listView.currentIndex = index - 1
        } else {
            // listView.currentIndex = 0
            index = 0
        }

        return index
    }

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
            }

            // TODO: Disabled project currenty selected
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
                        color: listView.isCurrentItem ? "black" : "white"
                    }

                    MouseArea {
                        anchors.fill: parent
                        acceptedButtons: Qt.LeftButton | Qt.RightButton
                        onClicked: (mouse)=> {

                            listView.currentIndex = index
                            console.log("listView.currentIndex: ", listView.currentIndex)
                            app_controller.project_list_controller.select_project(listView.currentIndex)
                            app_controller.task_table_controller.task_table_model.refresh_table(app_controller.project_list_controller.selected_project_id)

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
                                let new_index = root.reset_index(listView.currentIndex)
                                console.log("NEW INDEX: ", new_index)

                                app_controller.task_table_controller.task_table_model.refresh_table(app_controller.project_list_controller.selected_project_id)
                                app_controller.project_list_controller.select_project(new_index)
                                app_controller.project_list_controller.delete_project(app_controller.project_list_controller.selected_project_id)
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
