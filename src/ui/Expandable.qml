import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Rectangle {
    property int header_height: 50
    property string header_color: "pink"
    property int header_border: 2
    property string header_border_color: "#F8D64F"
    property string header_text_color: "white"
    property bool expanded
    property string headerText: ""
    property int _spacing: 5
    property int _total_height: root.header_height + tasksTable.contentHeight + _spacing

    id: root
    color: "transparent"
    implicitHeight: expanded ? _total_height : root.header_height

    /*
    onExpandedChanged: {

    }
    */

    ColumnLayout {
        anchors.fill: parent
        spacing: 0

        // HEADER
        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: false
            height: header_height

            color: header_color
            border.width: header_border
            border.color: header_border_color

            RowLayout {
                id: header
                anchors.fill: parent
                anchors.leftMargin: 30

                /*
                QtObject {
                    id: d
                    readonly property int rotationAngle: root.expanded ? 90 : 0
                }
                */

                // TODO: modify this by a svg image
                Text {
                    id: arrow
                    text: root.expanded ? "v" : ">"
                    //font.bold: true
                    font.pixelSize: 16
                    color: header_text_color
                    /*
                    rotation: d.rotationAngle
                    Behavior on rotation { NumberAnimation { duration: 150 } }
                    */
                }

                Text {
                    text: headerText
                    font.pixelSize: 16
                    font.weight: Font.Bold
                    font.capitalization: Font.AllUppercase
                    color: header_text_color
                }

            }

            MouseArea {
                anchors.fill: parent
                onReleased: {
                    root.expanded = !root.expanded
                }
            }

        }

        TasksTable {
            id: tasksTable

            implicitWidth: 100
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.leftMargin: 40
            Layout.topMargin: 5

            tasks_spacing: 5
            visible: root.expanded
        }

    }

}
