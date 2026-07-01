import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Rectangle {
    id: projectsList
    property string taskName: "Name of the task"
    property string description: "Description of the task"
    property string endDate: ""
    property string state: ""
    property string type: ""

    radius: 8
    border.color: "#dddddd"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 5

        Label {
            Layout.fillWidth: true
            Layout.fillHeight: true
            text: taskName
        }

        Label {
            Layout.fillWidth: true
            Layout.fillHeight: true
            text: description
        }

        // Task Info Panel

        // Buttons Panel
        RowLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.margins: 5
            spacing: 5

            Button {
                text: "Edit"
            }

            Button {
                text: "Cancel"
            }

            Button {
                text: "Save"
            }
        }
    }
}
