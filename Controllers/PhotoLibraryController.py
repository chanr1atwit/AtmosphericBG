# PhotoLibraryController class, last edited 6/25/2022
import sys
from PyQt5.QtWidgets import QApplication
from Views.MainGUI import *
from Views.PhotoLibraryGUI import *
from Views.SettingsGUI import *


class PhotoLibraryController:
    # Creates the models
    def __init__(self):     
        # Models
        

        # Subcontrollers
        #self.samplingTimerController = SamplingTimerController()
        pass
        
    def openView(self, view):
        view.show()
