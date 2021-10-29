# Form implementation generated from reading ui file 'sofistik.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from pathlib import Path

from PyQt6.QtWidgets import QFileDialog, QWidget

from main import main

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(911, 539)

        self.OKButton = QtWidgets.QPushButton(Dialog)
        self.OKButton.setGeometry(QtCore.QRect(150, 10, 141, 61))
        self.OKButton.setStyleSheet("background-color: rgb(89, 255, 0);")
        self.OKButton.setObjectName("OKButton")

        self.Openfile = QtWidgets.QPushButton(Dialog)
        self.Openfile.setGeometry(QtCore.QRect(310, 10, 341, 51))
        self.Openfile.setObjectName("Openfile")
        self.Openfile.clicked.connect(self.open_DB)

        self.File_name = QtWidgets.QLabel(Dialog)
        self.File_name.setGeometry(QtCore.QRect(670, 20, 201, 31))
        self.File_name.setObjectName("File_name")

        self.pic = QtWidgets.QLabel(Dialog)
        self.pic.setGeometry(QtCore.QRect(0, 90, 791, 381))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.button_pushed()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.OKButton.setText(_translate("Dialog", "OK"))
        self.Openfile.setText(_translate("Dialog", "OpenDB"))
        self.File_name.setText(_translate("Dialog", "File name"))

    def button_pushed(self):
        self.OKButton.clicked.connect(lambda: self.action())

    def action(self):
        main(self.Openfile.file)
        self.pic.setPixmap(QtGui.QPixmap("./result/test_image_from_python.bmp"))
        self.pic.setScaledContents(True)
        self.pic.setObjectName("label")

    def open_DB(self):
        file_name, _ = QFileDialog.getOpenFileName(self, caption='Open Db file (.cdb, .txt)', filter='Db files (*.cdb *.txt)')
        self.Openfile.file = Path(file_name)
        self.File_name.setText(self.Openfile.file.name)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

# Timer app

# from sys import exit as sysExit
# from time import sleep as tmSleep
#
# from PyQt6.QtCore import QCoreApplication, QObject, QThread, pyqtSignal, pyqtSlot
# from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
# from PyQt6.QtWidgets import QPushButton, QLineEdit
#
#
# class Processor(QObject):
#     sigCount = pyqtSignal(int)
#
#     def __init__(self):
#         QObject.__init__(self)
#         self.Connected = True
#         self.StreamRdy = False
#         self.Count = 0
#         self.Delay = 0
#
#     def ProcessRunner(self):
#         while self.Connected:
#             if self.StreamRdy:
#                 self.Delay = 0
#                 self.Count += 1
#                 self.sigCount.emit(self.Count)
#                 tmSleep(0.5)
#             else:
#                 self.Count = 0
#                 self.Delay -= 1
#                 self.sigCount.emit(self.Delay)
#                 tmSleep(0.5)
#             QCoreApplication.processEvents()
#
#     @pyqtSlot()
#     def StartProcess(self):
#         self.StreamRdy = True
#
#     @pyqtSlot()
#     def PauseProcess(self):
#         self.StreamRdy = False
#
#
# class MainWindow(QWidget):
#     sigStrtUp = pyqtSignal()
#     sigPauser = pyqtSignal()
#
#     def __init__(self):
#         QWidget.__init__(self)
#
#         self.setWindowTitle('Main Window')
#         self.setGeometry(150, 150, 200, 200)
#
#         self.btnActivate = QPushButton('Start')
#         self.btnActivate.clicked.connect(self.Activated)
#
#         self.btnDeActivate = QPushButton('Pause')
#         self.btnDeActivate.clicked.connect(self.DeActivate)
#
#         self.btnExitApp = QPushButton('Quit')
#         self.btnExitApp.clicked.connect(self.ExitApp)
#
#         self.lneOutput = QLineEdit()
#
#         HBox = QHBoxLayout()
#         HBox.addWidget(self.btnActivate)
#         HBox.addWidget(self.btnDeActivate)
#         HBox.addWidget(self.btnExitApp)
#         HBox.addStretch(1)
#
#         VBox = QVBoxLayout()
#         VBox.addWidget(self.lneOutput)
#         VBox.addLayout(HBox)
#
#         self.setLayout(VBox)
#
#         self.EstablishThread()
#
#     def EstablishThread(self):
#         # Create the Object from Class
#         self.Prcssr = Processor()
#         # Assign the Database Signals to Slots
#         self.Prcssr.sigCount.connect(self.CountRecieve)
#         # Assign Signals to the Database Slots
#         self.sigStrtUp.connect(self.Prcssr.StartProcess)
#         self.sigPauser.connect(self.Prcssr.PauseProcess)
#
#         # Create the Thread
#         self.ThredHolder = QThread()
#         # Move the Listener to the Thread
#         self.Prcssr.moveToThread(self.ThredHolder)
#         # Assign the Listener Starting Function to the Thread Call
#         self.ThredHolder.started.connect(self.Prcssr.ProcessRunner)
#         # Start the Thread which launches Listener.Connect( )
#         self.ThredHolder.start()
#
#     @pyqtSlot(int)
#     def CountRecieve(self, Count):
#         self.lneOutput.setText('Count : ' + str(Count))
#
#     def Activated(self):
#         self.sigStrtUp.emit()
#
#     def DeActivate(self):
#         self.sigPauser.emit()
#
#     def ExitApp(self):
#         sysExit()
#
#
# if __name__ == '__main__':
#     MainThred = QApplication([])
#
#     MainGui = MainWindow()
#     MainGui.show()
#
#     sysExit(MainThred.exec())
