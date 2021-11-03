from pathlib import Path

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog

from sofistik.settings import SOFISTIK_YEAR
from sofistik.sof_windows.sofistik_ui import SofistikUI
from sofistik.sof_windows.windows import AskPlateUI
from sofistik.sofistik_data_objects import get_plate_group
from sofistik.sofistik_discover import Sofistik
from sofistik.utils import logger


class MainUI(SofistikUI):

    def after_setup_ui(self):
        self.actionOpen_database.triggered.connect(self.open_db)
        self.button_pushed()

    def open_db(self):
        file_name, _ = QFileDialog.getOpenFileName(caption='Open database file',
                                                   filter='Db files (*.cdb *.txt)')
        self.database = Path(file_name)
        self.db_name.setText(f'Data base: {self.database.name}')
        self.sofistik = Sofistik(sofistik_year=SOFISTIK_YEAR, filename=self.database)
        self.ask_plate_number_dialog = QtWidgets.QDialog()
        self.ask_plate_number = PlateSelect(self.sofistik, self.ask_plate_number_dialog)
        self.ask_plate_number.base_setup_ui()
        self.ask_plate_number.after_setup_ui()

        self.ask_plate_number_dialog.show()


class PlateSelect(AskPlateUI):

    def __init__(self, sofistik: Sofistik, dialog):
        super().__init__(sofistik, dialog)

    def after_setup_ui(self):
        self.select_plate_OK.clicked.connect(self.plate_selected)

    def plate_selected(self):

        plate_group = get_plate_group(self.sofistik, int(self.plate_number.text()))
        try:
            ui.plate_number_setter(f'Plate group: {plate_group}')
        except Exception as e:
            logger.error(e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainUI()
    ui.base_setup_ui(MainWindow)
    ui.after_setup_ui()
    MainWindow.show()
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
