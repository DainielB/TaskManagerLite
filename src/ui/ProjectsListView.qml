import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Universal

import TaskManagerLite 1.0


Rectangle {
    // property alias model: projectsListModel
    id: root

    radius: 4
    border.color: "#dddddd"
    Layout.fillHeight: true
    Layout.fillWidth: true

    Universal.theme: Universal.Light

    ProjectsListModel {
        id: projectsListModel
    }

    function addProject(name, description, limitDate, color) {
        projectsListModel.add_project(name, description, limitDate, color)
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
            spacing: 2
            highlight: Rectangle { color: "orange" }
            // spacing: (parent.height / projectsListModel.num_projects()) // Divide number of projects / screen height (?)

            ScrollBar.vertical: ScrollBar {}

            // model: ProjectsListModel


            model: ListModel {
                id: listModel
                ListElement {
                    name: "Project 1"
                }
                ListElement {
                    name: "Project 2"
                }
            }


            Component {
                id: projectDelegate
                Item {
                    width: listView.width
                    height: 48
                    // color: listView.isCurrentItem ? "#d0e8ff" : "white"

                    Text {
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: 10
                        text: name
                        color: listView.isCurrentItem ? "#d0e8ff" : "black"
                    }

                    MouseArea {
                        anchors.fill: parent
                        onClicked: listView.currentIndex = index
                    }
                }
            }

            delegate: projectDelegate

            /*
            delegate: Rectangle {
                width: listView.width
                height: listView.height
                color: ListView.isCurrentItem ? "#d0e8ff" : "white"

                Text {
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.left: parent.left
                    anchors.leftMargin: 10
                    text: name
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: listView.currentIndex = index
                }
            }
            */

        }

        RowLayout {
            spacing: 10

            Item {
                Layout.alignment: Qt.AlignHCenter
                Layout.fillWidth: true
                Layout.fillHeight: true

                Button {
                    anchors.bottom: parent.bottom
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.bottomMargin: 20
                    enabled: true
                    highlighted: false
                    font.bold: true
                    width: 150
                    text: "+ New Project"

                    onReleased: projectDialog.open()
                }
            }

        }

    }

}
