import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Item {
    property bool expanded: false

    Layout.fillWidth: true
    Layout.fillHeight: true

    /*
    onExpandedChanged: {

    }
    */

    // Works like the header
    Rectangle {
        property string headerText: ""

        Layout.fillWidth: true
        Layout.fillHeight: true
        color: "#f0f0f0"


    }
}
