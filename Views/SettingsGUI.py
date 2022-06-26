# SettingsGUI class, last edited 6/23/2022
from PyQt5 import QtCore as QtC
from PyQt5 import QtWidgets as QtW

class SettingsGUI:
    # This function sets up the SettingsGIU view
    # NOTE: Uses a reference to the controller
    #       that created this View
    def __init__(self, controller):
        # Access to controller functions that do the work
        self.controller = controller

        # Window setup
        self.window = QtW.QMainWindow()
        self.window.setGeometry(0, 0, 500, 500)
        self.window.setWindowTitle("Atmospheric BG - Advanced Settings")
        self.window.setWindowModality(QtC.Qt.ApplicationModal)

        
        # Buttons on View
        mainButton = QtW.QPushButton("Back", self.window)
        mainButton.setGeometry(QtC.QRect(100,400,131,40))
        mainButton.clicked.connect(self.mainView)

    # Show the PhotoLibraryGUI dialog
    def show(self):
        self.window.show()

    def hide(self):
        self.window.hide()

    # List of connected views
    def mainView(self):
        self.hide()
