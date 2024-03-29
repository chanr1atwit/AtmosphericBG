# MainGUI subclass, last edited 6/27/2022
from PyQt5 import QtWidgets as QtW
from PyQt5.QtGui import QPainter as Qp
from PyQt5 import QtCore as QtC
from Views.GUI import *


class MainGUI(GUI):
    # This function sets up the MainGUI view
    # NOTE: Uses a reference to the controller
    #       that created this View
    def __init__(self, controller):
        # Call to super init
        # Window and controller defined by GUI superclass
        super().__init__(controller, 900, 500, "Atmospheric BG")
        
        ## Objects on View
        ## Future work, not necessary for the app to
        ## function but would be cool nonetheless
        #self.picture = label that updates on screen changing through app
        
        # Lines on View
        line = QtW.QFrame(self)
        line.setGeometry(QtC.QRect(0, 400, 900, 2))
        line.setFrameShadow(QtW.QFrame.Plain)
        line.setLineWidth(2)
        line.setFrameShape(QtW.QFrame.HLine)

        # Labels on View
        self.imageLabel = QtW.QLabel("Currently Chosen Image:", self)
        self.imageLabel.setGeometry(QtC.QRect(30, 10, 471, 16))

        #self.visualizerLabel = QtW.QLabel("Selected App:", self)
        #self.visualizerLabel.setGeometry(QtC.QRect(50, 450, 291, 16))
        
        # Buttons on View
        libraryButton = QtW.QPushButton("Photo Library", self)
        libraryButton.setGeometry(QtC.QRect(40, 440, 180, 40))
        libraryButton.clicked.connect(self.controller.photoLibraryView)

        settingsButton = QtW.QPushButton("Advanced Settings", self)
        settingsButton.setGeometry(QtC.QRect(360, 440, 180, 40))
        settingsButton.clicked.connect(self.controller.settingsView)
        
        selectionButton = QtW.QPushButton("Selection Menu", self)
        selectionButton.setGeometry(QtC.QRect(680, 440, 180, 40))
        selectionButton.clicked.connect(self.controller.selectionView)


        #visualizerButton = QtW.QPushButton("Select Visualizer", self)
        #visualizerButton.setGeometry(QtC.QRect(560, 400, 131, 40))
        #visualizerButton.clicked.connect(self.controller.visualizerView)

    # Perform all necessary closing actions
    # Signals end of program, write to config file
    # Close sockets to WSL
    def closeEvent(self, event):
        self.controller.writeConfiguration()
        self.controller.resetBackground()
        self.controller.requestClose()
        self.controller.hideAll()
        event.accept()
