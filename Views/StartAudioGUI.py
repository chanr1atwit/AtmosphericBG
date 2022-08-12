from PyQt5 import QtCore as QtC
from PyQt5 import QtWidgets as QtW

from Views.GUI import *

class StartAudioGUI(GUI):
    #remember to add controller back
    def __init__(self, controller):
        # Access to controller functions that do the work
        super().__init__(controller, 250, 250, "Atmospheric BG - App Selection")

        #GUI to record/stop recording
        self.startRecord = QtW.QPushButton("Record Audio", self)
        self.startRecord.setGeometry(QtC.QRect(55, 25, 131, 40))   
        self.startRecord.clicked.connect(self.controller.start)

        self.endRecord = QtW.QPushButton("End Recording", self)
        self.endRecord.setGeometry(QtC.QRect(55, 75, 131, 40)) 
        self.endRecord.setEnabled(False)
        self.endRecord.clicked.connect(self.controller.stop)   
        
        
        backButton = QtW.QPushButton("Back", self) 
        backButton.setGeometry(QtC.QRect(55,125,131,40))  
        backButton.clicked.connect(self.mainView) 
        
     # List of connected views
    def mainView(self):
        self.hide()
 