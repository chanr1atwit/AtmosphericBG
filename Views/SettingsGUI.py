# SettingsGUI class, last edited 6/23/2022
from PyQt5 import QtCore as QtC
from PyQt5 import QtWidgets as QtW

from Views.GUI import *

class SettingsGUI(GUI):
    # This function sets up the SettingsGIU view
    # NOTE: Uses a reference to the controller
    #       that created this View
    def __init__(self, controller):
        super().__init__(controller, 1500, 800, "Atmospheric BG - Advanced Settings")


        # Access to controller functions that do the work
        self.controller = controller

        # Window setup
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Atmospheric BG - Advanced Settings")
        self.setWindowModality(QtC.Qt.ApplicationModal)

        
        # Buttons on View
        mainButton = QtW.QPushButton("Back", self)
        mainButton.setGeometry(QtC.QRect(100,400,131,40))
        mainButton.clicked.connect(self.mainView)

    def mainView(self):
        self.hide()
