# SettingsGUI class, last edited 6/23/2022
from PyQt5 import QtCore as QtC
from PyQt5 import QtWidgets as QtW

from Views.GUI import *

class SettingsGUI(GUI):
    # This function sets up the SettingsGIU view
    # NOTE: Uses a reference to the controller
    #       that created this View
    def __init__(self, controller):
        super().__init__(controller, 800, 800, "Atmospheric BG - Advanced Settings")

        # Window setup
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Atmospheric BG - Advanced Settings")
        self.setWindowModality(QtC.Qt.ApplicationModal)
        
        # Buttons on View
        backButton = QtW.QPushButton("Back", self)
        backButton.setGeometry(QtC.QRect(600,700,131,40))
        backButton.clicked.connect(self.mainView)

        # Labels
        plLabel = QtW.QLabel("Photo Library Settings", self)
        plLabel.setGeometry(QtC.QRect(50, 50, 471, 16))

        ## Check boxes
        #plCB = QtW.QCheckBox("Enable Photo Library", self)
        #plCB.setGeometry(QtC.QRect(50, 75, 111, 20))
        #plCB.setChecked(self.controller.changePLState())
        #plCB.stateChanged.connect(self.controller.changePLState)

        #dynamicCB = QtW.QCheckBox("Enable Dynamic Backgrounds", self)
        #dynamicCB.setGeometry(QtC.QRect(50, 100, 111, 20))
        #dynamicCB.setChecked(self.controller.getDynamicState())
        #dynamicCB.stateChanged.connect(self.controller.changeDynamicState)

    def mainView(self):
        self.hide()
