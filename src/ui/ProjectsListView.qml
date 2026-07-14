import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Rectangle {
    id: root
    color: "#2A1F2D"

    radius: 4
    border.color: "#56E39F"
    Layout.fillHeight: true
    Layout.fillWidth: true

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

            model: app_controller.project_list_controller.project_list_model

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
                        text: projectDialog.projectName.text // TODO: Esto es lo que hace que cuando se cree un proyecto nuevo,
                                                            // los que ya hay en la lista se actualicen automáticamente con el nombre
                                                            // que se está poniendo en el textfield
                        color: listView.isCurrentItem ? "#d0e8ff" : "black"
                    }

                    MouseArea {
                        anchors.fill: parent
                        onClicked: listView.currentIndex = index
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
                    background: Rectangle {
                        implicitWidth: 100
                        implicitHeight: 40
                        enabled: true
//                        opacity: enabled ? 1 : 0.3
                        color: "#56E39F"
                    }
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
