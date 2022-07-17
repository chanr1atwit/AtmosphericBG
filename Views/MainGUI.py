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
        
        # Objects on View
        #self.picture = Qp.drawImage()
        
        # Lines on View
        line = QtW.QFrame(self)
        line.setGeometry(QtC.QRect(520, 0, 2, 500))
        line.setFrameShadow(QtW.QFrame.Plain)
        line.setLineWidth(2)
        line.setFrameShape(QtW.QFrame.VLine)

        line2 = QtW.QFrame(self)
        line2.setGeometry(QtC.QRect(0, 410, 520, 2))
        line2.setFrameShadow(QtW.QFrame.Plain)
        line2.setLineWidth(2)
        line2.setFrameShape(QtW.QFrame.HLine)

        # Labels on View
        self.imageLabel = QtW.QLabel("Currently Chosen Image:", self)
        self.imageLabel.setGeometry(QtC.QRect(30, 10, 471, 16))

        self.visualizerLabel = QtW.QLabel("Selected App:", self)
        self.visualizerLabel.setGeometry(QtC.QRect(50, 450, 291, 16))

        # Check boxes
        self.visualizerCB = QtW.QCheckBox("Enable Visualizer", self)
        self.visualizerCB.setGeometry(QtC.QRect(570, 360, 111, 20))
        
        self.visualizerDemoCD = QtW.QCheckBox("Visualizer Demo", self)
        self.visualizerDemoCD.setGeometry(QtC.QRect(740, 360, 111, 20))
        
        # Buttons on View
        libraryButton = QtW.QPushButton("Photo Library", self)
        libraryButton.setGeometry(QtC.QRect(30, 340, 131, 40))
        libraryButton.clicked.connect(self.controller.photoLibraryView)

        settingsButton = QtW.QPushButton("Advanced Settings", self)
        settingsButton.setGeometry(QtC.QRect(360, 340, 131, 40))
        settingsButton.clicked.connect(self.controller.settingsView)
        
        selectionButton = QtW.QPushButton("Selection Menu", self)
        selectionButton.setGeometry(QtC.QRect(360, 440, 131, 40))
        selectionButton.clicked.connect(self.controller.selectionView)

        #visualizerButton = QtW.QPushButton("Select Visualizer", self)
        #visualizerButton.setGeometry(QtC.QRect(560, 400, 131, 40))
        #visualizerButton.clicked.connect(self.controller.visualizerView)
