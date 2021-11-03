from PyQt6 import QtGui

from sofistik.sofistik_data_objects import quad_dict_from_db
from sofistik.sof_windows.windows import MainWindowUI


class SofistikUI(MainWindowUI):

    def __init__(self):
        self.sofistik = None
        self.database = None
        self.ask_plate_number = None

    # def button_pushed(self):
    #     self.OKButton.clicked.connect(lambda: self.action())

    def action(self, db_index: int):
        quad_dict_from_db(self.sofistik, db_index=db_index)
        self.plate_picture.setPixmap(QtGui.QPixmap("./result/test_image_from_python.bmp"))
        self.plate_picture.setScaledContents(True)
        self.plate_picture.setObjectName("label")

    def plate_group_setter(self, text: str):
        self.plate_group.setText(text)
