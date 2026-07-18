import QtQuick
import QtQuick.Layouts
import QtQuick.Controls


Rectangle {
    Layout.fillWidth: true
    Layout.fillHeight: true

    ColumnLayout {

        RowLayout {
            Text { text: "Task"; Layout.preferredWidth: 200 }
            Text { text: "End Date"; Layout.preferredWidth: 120 }
            Text { text: "Status"; Layout.preferredWidth: 100 }
            Text { text: "Priority"; Layout.preferredWidth: 80 }
            // Text { text: "Progress"; Layout.preferredWidth: 80 }
            Text { text: "Type"; Layout.fillWidth: true }
        }

        ListView {
            Layout.fillWidth: true
            Layout.fillHeight: true
            model: tasksModel
            delegate: taskRowDelegate  // RowLayout con cada "columna" como componente distinto
        }
    }

}
