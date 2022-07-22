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

        # Check boxes
        self.plCB = QtW.QCheckBox("Enable Photo Library", self)
        self.plCB.setGeometry(QtC.QRect(50, 75, 170, 20))
        self.plCB.toggled.connect(lambda: self.controller.setPLState(self.plCB.isChecked()))

        self.dynamicCB = QtW.QCheckBox("Enable Dynamic Backgrounds", self)
        self.dynamicCB.setGeometry(QtC.QRect(50, 100, 170, 20))
        self.dynamicCB.toggled.connect(lambda: self.controller.setDynamicState(self.dynamicCB.isChecked()))

    def show(self):
        super().show()
        self.plCB.setChecked(self.controller.getPLState())
        self.dynamicCB.setChecked(self.controller.getDynamicState())

    def mainView(self):
        self.hide()
