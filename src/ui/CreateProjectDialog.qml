import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Universal


Dialog {
    Universal.theme: Universal.Light

    id: createProject
    title: "createProject"
    modal: true
    anchors.centerIn: parent

    ColumnLayout {
        Layout.fillWidth: true
        Layout.fillHeight: true
        Layout.margins: 10
        spacing: 5

        TextField {
            id: projectName
            Layout.margins: 10
            Layout.fillWidth: true
            Layout.fillHeight: false
            text: "Project Name"
        }

        TextField {
            id: projectDescription
            Layout.margins: 10
            Layout.fillWidth: true
            Layout.fillHeight: true
            text: "Project Description (Optional)"
        }

        RowLayout {
            Layout.margins: 10
            Layout.fillWidth: true
            Layout.fillHeight: false
            spacing: 5



        }

    }

    standardButtons: Dialog.Cancel | Dialog.Ok

    onAccepted: console.log("Pulsado OK")
    onRejected: console.log("Pulsado Cancelar")
}
