# SettingsGUI class, last edited 6/23/2022
from subprocess import _TXT
from PyQt5 import QtCore as QtC
from PyQt5 import QtWidgets as QtW
from PyQt5 import QtGui as QtG

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


### WIDGETS FOR SAMPLING TIMER
        waitLabel = QtW.QLabel(self)
        waitLabel.setGeometry(QtC.QRect(300,80,225,20))

        self.wait = QtW.QLineEdit(self.controller.getConfiguration(
            "Sampling", "wait", str) , self)
        self.wait.setGeometry(QtC.QRect(300,100,225,20))
        self.wait.setValidator(QtG.QIntValidator(30,300))
        self.wait.textChanged.connect(lambda: self.controller.setConfiguration(
            "Sampling", "wait", self.wait.text()))

### WIDGETS FOR PHOTO LIBRARY
        # Base location for sections
        plX = 50
        plY = 50

        # Labels
        plLabel = QtW.QLabel("Photo Library Settings", self)
        plLabel.setGeometry(QtC.QRect(plX, plY, 471, 16))

        xLabel = QtW.QLabel("X", self)
        xLabel.move(plX+60,plY+117)
        
        sizeLabel = QtW.QLabel("Custom Size", self)
        sizeLabel.setGeometry(QtC.QRect(plX,plY+75,100,16))

        widthLabel = QtW.QLabel("Width", self)
        widthLabel.setGeometry(QtC.QRect(plX,plY+100,100,16))

        heightLabel = QtW.QLabel("Height", self)
        heightLabel.setGeometry(QtC.QRect(plX+75,plY+100,100,16))

        # Text boxes
        self.width = QtW.QLineEdit(self.controller.getConfiguration(
            "Settings", "width", str), self)
        self.width.setGeometry(QtC.QRect(plX,plY+125,50,16))
        self.width.setValidator(QtG.QIntValidator(100,10000))
        self.width.textChanged.connect(lambda: self.controller.setConfiguration(
            "Settings", "width", self.width.text()))

        self.height = QtW.QLineEdit(self.controller.getConfiguration(
            "Settings", "height", str), self)
        self.height.setGeometry(QtC.QRect(plX+75,plY+125,50,16))
        self.height.setValidator(QtG.QIntValidator(100,10000))
        self.height.textChanged.connect(lambda: self.controller.setConfiguration(
            "Settings", "height", self.height.text()))

        # Check boxes
        self.plCB = QtW.QCheckBox("Enable Photo Library", self)
        self.plCB.setGeometry(QtC.QRect(plX, plY+25, 170, 20))
        self.plCB.toggled.connect(lambda: self.controller.setPLState(self.plCB.isChecked()))
        self.plCB.setChecked(self.controller.getConfiguration("PhotoLibrary", "library", bool))

        self.dynamicCB = QtW.QCheckBox("Enable Dynamic Backgrounds", self)
        self.dynamicCB.setGeometry(QtC.QRect(plX, plY+50, 170, 20))
        self.dynamicCB.toggled.connect(lambda: self.controller.setDynamicState(self.dynamicCB.isChecked()))
        self.dynamicCB.setChecked(self.controller.getConfiguration("PhotoLibrary", "dynamic", bool))

### WIDGETS FOR LED CONTROLLER
        ledX = 50
        ledY = 300

        findProgram = QtW.QPushButton("Re-assign LED App", self)
        findProgram.setGeometry(QtC.QRect(ledX, ledY, 170, 50))
        findProgram.clicked.connect(self.controller.findLEDProgram)

        runProgram = QtW.QPushButton("Run LED App", self)
        runProgram.setGeometry(QtC.QRect(ledX, ledY + 75, 170, 50))
        runProgram.clicked.connect(self.controller.runLEDApp)

### WIDGETS FOR THEME CHANGER
        tX = 400
        tY = 300

        self.tealTheme = QtW.QRadioButton("Teal", self)
        self.tealTheme.setGeometry(QtC.QRect(tX, tY, 170, 50))
        self.tealTheme.toggled.connect(lambda : self.controller.setTheme('light_teal.xml'))

        self.blueTheme = QtW.QRadioButton("Teal", self)
        self.blueTheme.setGeometry(QtC.QRect(tX, tY+20, 170, 50))
        self.blueTheme.toggled.connect(lambda : self.controller.setTheme('light_blue.xml'))
        
        self.redTheme = QtW.QRadioButton("Teal", self)
        self.redTheme.setGeometry(QtC.QRect(tX, tY+40, 170, 50))
        self.redTheme.toggled.connect(lambda : self.controller.setTheme('dark_red.xml'))

        self.dynamicTheme = QtW.QRadioButton("Dynamic", self)
        self.dynamicTheme.setGeometry(QtC.QRect(tX, tY+60, 170, 50))
        self.dynamicTheme.toggled.connect(lambda : self.controller.setTheme('default'))

    # Sets the radio button to the proper theme
    # Doesn't actually set the theme, that is
    # done in the core controller
    def setOpenTheme(self, theme):
        if theme == 'light_teal.xml':
            self.tealTheme.setChecked(True)
        elif theme == 'light_blue.xml':
            self.blueTheme.setChecked(True)
        elif theme == 'dark_red.xml':
            self.redTheme.setChecked(True)
        else:
            self.dynamicTheme.setChecked(True)

    def show(self):
        super().show()
        self.setOpenTheme(self.controller.getTheme())
        self.plCB.setChecked(self.controller.getPLState())
        self.dynamicCB.setChecked(self.controller.getDynamicState())

    def hide(self):
        self.controller.setCustomDims(self.width.text(), self.height.text())
        self.controller.setWaitTime(self.wait.text())
        super().hide()

    def mainView(self):
        self.hide()
