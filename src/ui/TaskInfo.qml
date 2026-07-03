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
            Layout.fillWidth: false
            Layout.margins: 10
            Layout.fillHeight: false
            Layout.alignment: Qt.AlignHCenter
            text: taskName
        }

        Label {
            Layout.margins: 10
            Layout.fillWidth: true
            Layout.fillHeight: true
            // Layout.alignment: Qt.AlignHCenter
            text: description
        }

        // Task Info Panel
        GridLayout {
            columns: 2
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.margins: 10

            ColumnLayout {
                spacing: 5

                Label {
                    text: "Start Date"
                }

                TextField {
                    id: startDate
                    Layout.fillWidth: true
                    // Layout.fillHeight: true
                    enabled: false
                    text: "02-06-26"
                }
            }

            ColumnLayout {
                spacing: 5

                Label {
                    text: "End Date"
                }

                TextField {
                    id: endDate
                    Layout.fillWidth: true
                    // Layout.fillHeight: true
                    enabled: false
                    text: "28-06-26"
                }

            }

            ColumnLayout {
                spacing: 5

                Label {
                    text: "Status"
                }

                TextField {
                    id: taskStatus
                    Layout.fillWidth: true
                    // Layout.fillHeight: true
                    enabled: false
                    text: "In Progress"
                }
            }

            ColumnLayout {
                spacing: 5

                Label {
                    text: "Priority"
                }

                TextField {
                    id: priority
                    Layout.fillWidth: true
                    // Layout.fillHeight: true
                    enabled: false
                    text: "High"
                }
            }

        }

        // Buttons Panel
        RowLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.margins: 10
            Layout.alignment: Qt.AlignRight
            spacing: 5

            Button {
                text: "Edit"
            }

            /*
            Button {
                text: "Cancel"
            }
            */

            Button {
                text: "Save"
            }
        }
    }
}
