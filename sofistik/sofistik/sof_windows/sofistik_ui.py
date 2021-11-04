from PyQt6 import QtGui

from sofistik.sof_windows.pyqt_windows import MainWindowUI
from sofistik.sofistik_data_objects import quad_dict_from_db
from sofistik.database.commands import db_insert_or_update_quad
from sofistik.utils import create_image


class SofistikUI(MainWindowUI):
    """
    Sofistik window after MainWindow from PyQt6 \n
    Sofistik class: sofistik \n
    Path(): database \n
    PyQtWindow: ask_area_number \n
    action: action()
    """
    def __init__(self):
        self.sofistik = None
        self.database = None
        self.ask_area_number = None

    # def button_pushed(self):
    #     self.OKButton.clicked.connect(lambda: self.action())

    def action_on_group_chosen(self, area: int, group: int) -> None:
        """
        Extract quads from sofistik cdb, add it to SQL db and create image

        :param area: User select what area to display
        :param group: Plate group just for check the data is correct

        :return: Insert quads in DB and show created image
        """
        quads = quad_dict_from_db(self.sofistik, area=area)
        for quad, nodes in quads.items():
            db_insert_or_update_quad(update_obj=False, quad_number=quad, nodes=quads[quad], area=area, group=group,
                                     banding_moment_mxx=0, banding_moment_myy=0, banding_moment_mxy=0)

        # Create image with quads
        create_image(quad_dict=quads, image_name='result/test_image_from_python.bmp')

        # Show image on main template
        self.plate_picture.setPixmap(QtGui.QPixmap("./result/test_image_from_python.bmp"))
        self.plate_picture.setScaledContents(True)
        self.plate_picture.setObjectName("label")

    def plate_group_setter(self, text: str) -> None:
        """
        Set plate group to plate group label

        :param text: Set this text to plate_group label
        """
        self.plate_group.setText(text)
