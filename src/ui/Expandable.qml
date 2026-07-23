import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Rectangle {
    property int new_width
    property int new_height
    property bool expanded: false
    property string headerText: ""

    id: root

    implicitWidth: new_width
    implicitHeight: new_height
    color: "red"
    border.width: 1
    border.color: "black"

    /*
    onExpandedChanged: {

    }
    */

    ColumnLayout {
        anchors.fill: parent

        // HEADER
        Item {
            Layout.fillWidth: true
            Layout.fillHeight: true

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
                    text: "▶"
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
                    console.log("EY")
                    root.expanded = !root.expanded
                }
            }

        }

    }

    TasksTable {
        id: tasksTable

        //Layout.fillWidth: true
        //Layout.fillHeight: true
        //Layout.leftMargin: 40
        anchors.fill: root
        anchors.leftMargin: 40

        visible: root.expanded
    }

}
