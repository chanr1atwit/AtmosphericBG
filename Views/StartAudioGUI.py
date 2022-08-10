from PyQt5 import QtCore as QtC
from PyQt5 import QtWidgets as QtW
import threading


from Views.GUI import *

class StartAudioGUI(GUI):
    #remember to add controller back
    def __init__(self, controller):
        # Access to controller functions that do the work
        super().__init__(controller, 250, 250, "Atmospheric BG - App Selection")

        #GUI to record/stop recording
        self.thread = None
        startRecord = QtW.QPushButton("Record Audio", self)
        startRecord.setGeometry(QtC.QRect(55, 25, 131, 40))   
        startRecord.clicked.connect(self.startFunction)

        endRecord = QtW.QPushButton("End Recording", self)
        endRecord.setGeometry(QtC.QRect(55, 75, 131, 40)) 
        endRecord.clicked.connect(self.endFunction)    
        
        backButton = QtW.QPushButton("Back", self) 
        backButton.setGeometry(QtC.QRect(55,125,131,40))  
        backButton.clicked.connect(self.mainView) 
        
    #runs detection on a thread
    def startFunction(self):
        self.thread = threading.Thread(target = self.controller.audioToWav)
        self.thread.start()

    def endFunction(self):
        if self.thread is None:
                return
        else:
            pass
            #self.thread.stop()

     # List of connected views
    def mainView(self):
        self.hide()
 