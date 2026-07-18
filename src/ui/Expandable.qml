import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Rectangle { // Item
    property bool expanded: false
    property string headerText: "" // Might come from the outside/parent

    id: root
    color: "transparent"

    /*
    onExpandedChanged: {

    }
    */

    ColumnLayout {
        anchors.fill: parent

        // HEADER
        Rectangle {
            id: header
            Layout.fillWidth: true
            Layout.fillHeight: false
            Layout.leftMargin: 10
            color: "#f0f0f0"
            border.width: 1
            border.color: "#ccc"

            RowLayout {
                Layout.fillWidth: true
                Layout.fillHeight: true

                Text {
                    text: "▶"
                    font.pixelSize: 16
                    font.weight: Font.Bold
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                }

                Text {
                    text: headerText
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    font.pixelSize: 16
                    font.weight: Font.Bold
                    font.capitalization: Font.AllUppercase
                }
            }

        }

        /*
        TasksTable {
            Layout.fillWidth: true
            Layout.fillHeight: true
        }
        */

    }

}
