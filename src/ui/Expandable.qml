import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Rectangle {
    property int new_width
    property int new_height
    property int header_height: 50
    property string header_color: "pink"
    property bool expanded
    property string headerText: ""
    property int _spacing: 5
    property int _total_height: root.header_height + tasksTable.contentHeight + _spacing

    id: root
    color: "transparent" // "orange"
    implicitHeight: expanded ? _total_height : root.header_height

    /*
    onExpandedChanged: {
        console.log("headerText:", headerText,
                     "| header_height:", header_height,
                     "| tasksTable.contentHeight:", tasksTable.contentHeight,
                     "| _total_height:", _total_height,
                     "| root.implicitHeight:", implicitHeight,
                     "| root.height:", height)
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
            // Component.onCompleted: console.log("header width real:", width, "implicitWidth:", implicitWidth, "header height real:", height, "implicitHeight:", implicitHeight)

            color: header_color
            border.width: 1
            border.color: "black"

            RowLayout {
                id: header
                anchors.fill: parent
                anchors.leftMargin: 30
                //anchors.verticalCenter: parent.verticalCenter

                /*
                QtObject {
                    id: d
                    readonly property int rotationAngle: root.expanded ? 90 : 0
                }
                */

                // TODO: modify this by a svg image
                Text {
                    id: arrow
                    //text: "▶"
                    text: root.expanded ? "v" : ">"
                    //font.bold: true
                    font.pixelSize: 16
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
            //implicitHeight: 300
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.leftMargin: 40
            Layout.topMargin: 5

            tasks_spacing: 5
            visible: root.expanded
        }

    }

}
