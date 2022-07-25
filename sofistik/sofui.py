from pathlib import Path

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QFileDialog

from sofistik.database.utils import create_database, run_migrations
from sofistik.settings import DATABASE_NAME, SOFISTIK_YEAR
from sofistik.sof_windows.pyqt_windows import AskPlateUI
from sofistik.sof_windows.sofistik_ui import SofistikUI
from sofistik.sofistik_data_objects import get_plate_group
from sofistik.sofistik_discover import Sofistik
from sofistik.utils import logger


class MainUI(SofistikUI):
    """Main window of program"""

    def after_setup_ui(self) -> None:
        """Add action in File menu when database added"""

        self.calculate_button.clicked.connect(
            lambda: self.calculate_button_action(self.ask_area_number, self.plate_group.text())
        )

        self.choose_db_menu.triggered.connect(self.open_db)
        # self.button_pushed()

    def open_db(self) -> None:
        """Add and show new window with select area option"""

        file_name, _ = QFileDialog.getOpenFileName(caption='Open database file', filter='Db files (*.cdb *.txt)')
        self.database = Path(file_name)
        self.db_name.setText(f'Data base: {self.database.name}')

        self.sofistik = Sofistik(sofistik_year=SOFISTIK_YEAR, filename=self.database)

        # Add new area select window
        ask_plate_number_dialog = QDialog()
        self.ask_area_number = AreaSelect(self.sofistik, ask_plate_number_dialog)
        self.ask_area_number.base_setup_ui()
        self.ask_area_number.after_setup_ui()
        ask_plate_number_dialog.show()


class AreaSelect(AskPlateUI):
    """Ask area window"""

    def __init__(self, sofistik: Sofistik, dialog):
        self.area_number = None
        super().__init__(sofistik, dialog)

    def after_setup_ui(self):
        """Add select_area_OK button action"""
        self.select_area_OK.clicked.connect(self.area_selected)

    def area_selected(self):
        """
        Get plate group and set it on main UI to plate_group_label \n
        Extract quads from sofistik cdb, add it to SQL db and create image
        """
        area = int(self.area.text())
        group = get_plate_group(self.sofistik, area)
        try:
            ui.plate_group_area_setter(text=f'Plate group: {group} Area {area}')
            ui.ask_area_number = area
        except Exception as e:
            logger.error(e)


if __name__ == "__main__":
    database_file = Path(f'{DATABASE_NAME}')
    if not database_file.exists():
        create_database()
        run_migrations()
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainUI()
    ui.base_setup_ui(MainWindow)
    ui.after_setup_ui()
    MainWindow.show()
    sys.exit(app.exec())
