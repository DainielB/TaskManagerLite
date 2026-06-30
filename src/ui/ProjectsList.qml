import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Rectangle {
    id: projectsList
    property string projectName: "Project 1"

    color: "yellow"
    radius: 8
    border.color: "#dddddd"

    ColumnLayout {
        anchors.fill: parent

        ColumnLayout {
            Layout.alignment: Qt.AlignHCenter
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.topMargin: 20
            spacing: 30
            // Layout.verticalStretchFactor: 3

            Text {
                // text: root.projectName
                text: "Project 1"
                font.bold: true
            }

            Text {
                text: "Project 2"
                font.bold: true
            }

            Text {
                text: "Project 3"
                font.bold: true
            }

        }

        RowLayout {
            spacing: 10

            Item {
                Layout.alignment: Qt.AlignHCenter
                Layout.fillWidth: true
                Layout.fillHeight: true

                Button {
                    enabled: true
                    highlighted: false
                    text: "Aceptar"
                    anchors.bottom: parent.bottom
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.bottomMargin: 20
                }
            }

        }

    }
}
