import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Rectangle {
    property int new_width
    property int new_height
    property int header_height
    property string header_color
    property bool expanded: false
    property string headerText: ""
    property int _total_height: header.implicitHeight + (app_controller.task_table_controller.task_table_model.rowCount * tasksTable.implicitHeight)

    id: root
    color: "orange" // "transparent"

    /*
    onExpandedChanged: {

    }
    */

    ColumnLayout {
        anchors.fill: parent

        // HEADER
        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: false
            implicitHeight: header_height
            Component.onCompleted: console.log("header width real:", width, "implicitWidth:", implicitWidth, "header height real:", height, "implicitHeight:", implicitHeight)

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
                    text: ">"
                    font.bold: true
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
                    console.log("EY", root._total_height)
                    root.expanded = !root.expanded
                    root.implicitHeight = root.expanded ? 200 : root.header_height
                    //header.height = root.expanded ? 20 : root.header_height
                }
            }

        }

        TasksTable {
            id: tasksTable

            implicitWidth: 100
            implicitHeight: root._total_height
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.leftMargin: 40

            // visible: root.expanded
            height: root.expanded ? 10 : 0
            // arrow.text = root.expanded ? ">" : "<"
        }

    }

}
