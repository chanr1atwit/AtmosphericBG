import sys
from PyQt5 import uic
# from PySide2 import QtWidgets
import subprocess


from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QPushButton, QFileDialog
# from PyQt5 import QtWidgets
from qt_material import apply_stylesheet
# create the application and the main window

def open_a_program(self):
    try:
        # browse for an application
        path, _ = QFileDialog.getOpenFileName(self, 'Open a program', QtCore.QDir.rootPath(), '*.exe')

        # if an application is selected, and not cancelled
        if path != ('', ''):
            # run application
            subprocess.run([path])
    except Exception as e:
        print(e) # print exceptions

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("welcome.ui", self)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu = QtWidgets.QAction("&Open File", self)

        # window title and config
        self.title = "Menu Window"
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 200

        # create and configure button
        # also assigned shortcut Ctrl+O
        self.pushButton1 = QPushButton("ABG - LED", self)
        self.pushButton1.setShortcut("Ctrl+O")
        self.pushButton1.move(100, 60)
        self.pushButton1.setToolTip("ABG - LED")

        # on click functions for each button
        self.pushButton1.clicked.connect(self.open_a_program)

        # initialize main window
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

        # Call function when menu button is clicked
        self.actionLight.triggered.connect(self.light_teal)
        self.actionNeutral.triggered.connect(self.light_blue)
        self.actionDark.triggered.connect(self.dark_red)
        self.actionOpen_File = QtWidgets.QAction(self)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionOpen_File.setStatusTip("Open File")
        self.actionOpen_File.setShortcut('Ctrl+O')
        self.actionOpen_File.triggered.connect(self.file_open)
        self.menuFile.addAction(self.actionOpen_File)
        self.radioButton.clicked.connect(self.light_teal)
        self.radioButton_2.clicked.connect(self.light_blue)
        self.radioButton_3.clicked.connect(self.dark_red)

    def open_a_program(self):
        self.w = open_a_program(self) # calling the open_a_program function
        
    def file_open(self):
        name, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', options=QtWidgets.QFileDialog.DontUseNativeDialog)
        file = open(name, 'r')
        with file:
            text = file.read()
            self.text_output.setText(text)

        #Change theme when button is clicked
        
    def light_teal(self):
        apply_stylesheet(app, theme='light_teal.xml')

    def light_blue(self):
        apply_stylesheet(app, theme='light_blue.xml')

    def dark_red(self):
        apply_stylesheet(app, theme='dark_red.xml')

    def dynamic(self):
        apply_stylesheet()
    
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        UIWindow = UI()
        UIWindow.show()
        app.exec_()
if hasattr(app, 'exec'):
    app.exec()
else:
    app.exec_()
