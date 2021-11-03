from PyQt6 import QtGui

from main import main
from sofistik.sof_windows.windows import MainWindowUI


class SofistikUI(MainWindowUI):

    def __init__(self):
        self.sofistik = None
        self.database = None
        self.ask_plate_number = None

    def button_pushed(self):
        self.OKButton.clicked.connect(lambda: self.action())

    def action(self):
        main(self.database)
        self.plate_picture.setPixmap(QtGui.QPixmap("./result/test_image_from_python.bmp"))
        self.plate_picture.setScaledContents(True)
        self.plate_picture.setObjectName("label")

    def plate_number_setter(self, text: str):
        self.plate_group.setText(text)
