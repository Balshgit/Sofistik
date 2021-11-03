from pathlib import Path

from PyQt6.QtWidgets import QFileDialog

from main import main
from sofistik.settings import SOFISTIK_YEAR

from sofistik.sofistik_discover import Sofistik
from sofistik.utils import logger
from sofistik.sof_windows.windows import MainWindowUI, AskPlateUI

from PyQt6 import QtGui, QtWidgets


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


