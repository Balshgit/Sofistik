# Form implementation generated from reading ui file 'sofistik.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(911, 539)
        self.OKButton = QtWidgets.QPushButton(Dialog)
        self.OKButton.setGeometry(QtCore.QRect(150, 10, 141, 61))
        self.OKButton.setStyleSheet("background-color: rgb(89, 255, 0);")
        self.OKButton.setObjectName("OKButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 100, 911, 441))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../sofistik/result/test_image_from_python.bmp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Openfile = QtWidgets.QPushButton(Dialog)
        self.Openfile.setGeometry(QtCore.QRect(310, 10, 341, 51))
        self.Openfile.setObjectName("Openfile")
        self.File_name = QtWidgets.QLabel(Dialog)
        self.File_name.setGeometry(QtCore.QRect(670, 20, 201, 31))
        self.File_name.setObjectName("File_name")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.OKButton.setText(_translate("Dialog", "OK"))
        self.Openfile.setText(_translate("Dialog", "PushButton"))
        self.File_name.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())