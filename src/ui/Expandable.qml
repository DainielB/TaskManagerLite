import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Rectangle {
    property int new_width: 40
    property int new_height: 50
    property bool expanded: false
    property string headerText: ""

    id: root

    /*
    onExpandedChanged: {

    }
    */

    ColumnLayout {
        anchors.fill: parent

        // HEADER
        Rectangle {
            id: header

            Layout.preferredWidth: new_width
            Layout.preferredHeight: new_height
            Layout.leftMargin: 10

            color: "#5B6E86"
            border.width: 2
            border.color: "#ccc"
            visible: true

            RowLayout {
                //anchors.fill: parent
                //anchors.right: parent.right
                anchors.verticalCenter: parent.verticalCenter

                /*
                QtObject {
                    id: d
                    readonly property int rotationAngle: root.expanded ? 90 : 0
                }
                */

                Text {
                    id: arrow
                    text: "▶"
                    font.pixelSize: 16
                    font.weight: Font.Bold
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

            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.leftMargin: 50

            visible: root.expanded
        }

    }

}
