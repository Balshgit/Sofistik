from PyQt6 import QtCore, QtGui, QtWidgets

from sofistik.sofistik_discover import Sofistik


class MainWindowUI(object):
    def base_setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(1500, 900)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.db_name = QtWidgets.QLabel(self.centralwidget)
        self.db_name.setGeometry(QtCore.QRect(0, 10, 300, 50))
        self.db_name.setText("")
        self.db_name.setWordWrap(True)
        self.db_name.setObjectName("db_name")
        self.OKButton = QtWidgets.QPushButton(self.centralwidget)
        self.OKButton.setGeometry(QtCore.QRect(640, 20, 141, 61))
        self.OKButton.setStyleSheet("background-color: rgb(89, 255, 0);")
        self.OKButton.setObjectName("OKButton")
        self.plate_picture = QtWidgets.QLabel(self.centralwidget)
        self.plate_picture.setGeometry(QtCore.QRect(0, 130, 1400, 900))
        self.plate_picture.setText("")
        self.plate_picture.setPixmap(QtGui.QPixmap("../sofistik/result/test_image_from_python.bmp"))
        self.plate_picture.setScaledContents(True)
        self.plate_picture.setObjectName("plate_picture")
        self.plate_group = QtWidgets.QLabel(self.centralwidget)
        self.plate_group.setGeometry(QtCore.QRect(350, 10, 300, 50))
        self.plate_group.setText("")
        self.db_name.setWordWrap(True)
        self.plate_group.setObjectName("plate_group")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.actionOpen_database = QtGui.QAction(main_window)
        self.actionOpen_database.setObjectName("actionOpen_database")
        self.actionabout = QtGui.QAction(main_window)
        self.actionabout.setObjectName("actionabout")
        self.actionexit = QtGui.QAction(main_window)
        self.actionexit.setObjectName("actionexit")
        self.menuFile.addAction(self.actionOpen_database)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionexit)
        self.menuhelp.addAction(self.actionabout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.translate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def translate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OKButton.setText(_translate("MainWindow", "OK"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.actionOpen_database.setText(_translate("MainWindow", "Open database..."))
        self.actionabout.setText(_translate("MainWindow", "about"))
        self.actionexit.setText(_translate("MainWindow", "exit"))


class AskPlateUI(object):

    def __init__(self, sofistik: Sofistik, dialog):
        self.sofistik = sofistik
        self.plate_group = None
        self.ask_plate = dialog

    def base_setup_ui(self):
        self.ask_plate.setObjectName("Ask_plate")
        self.ask_plate.setEnabled(True)
        self.ask_plate.resize(169, 94)
        self.plate_number_lable_text = QtWidgets.QLabel(self.ask_plate)
        self.plate_number_lable_text.setGeometry(QtCore.QRect(10, 10, 161, 20))
        self.plate_number_lable_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.plate_number_lable_text.setObjectName("plate_number_lable_text")
        self.plate_number = QtWidgets.QSpinBox(self.ask_plate)
        self.plate_number.setGeometry(QtCore.QRect(20, 40, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.plate_number.setFont(font)
        self.plate_number.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.plate_number.setObjectName("plate_number")
        self.plate_number.setMaximum(1000000)
        self.select_plate_OK = QtWidgets.QPushButton(self.ask_plate)
        self.select_plate_OK.setGeometry(QtCore.QRect(100, 40, 51, 31))
        self.select_plate_OK.setStyleSheet("background-color: rgb(89, 255, 0);")
        self.select_plate_OK.setObjectName("select_plate_OK")
        self.select_plate_OK_pressed = QtGui.QAction(self.ask_plate)
        self.select_plate_OK_pressed.setObjectName("select_plate_OK_pressed")

        self.select_plate_OK.clicked.connect(self.ask_plate.hide)

        self.retranslateUi(self.ask_plate)
        QtCore.QMetaObject.connectSlotsByName(self.ask_plate)

    def retranslateUi(self, ask_plate):
        _translate = QtCore.QCoreApplication.translate
        ask_plate.setWindowTitle(_translate("Ask_plate", "Выбор пластины"))
        self.plate_number_lable_text.setText(_translate("Ask_plate", "Введите номер пластины"))
        self.select_plate_OK.setText(_translate("Ask_plate", "OK"))
        self.select_plate_OK_pressed.setText(_translate("Ask_plate", "plate_selected"))
        self.select_plate_OK_pressed.setToolTip(
            _translate("Ask_plate", "<html><head/><body><p>Select plate and press OK</p></body></html>"))
        self.select_plate_OK_pressed.setShortcut(_translate("Ask_plate", "Return"))
