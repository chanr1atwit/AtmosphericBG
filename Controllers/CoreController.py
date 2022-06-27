# CoreController class, last edited 6/20/2022
import sys
from PyQt5.QtWidgets import QApplication
from Views.MainGUI import *


class CoreController:
    # Create all elements of the app
    # Views, Controllers, possible Models
    def __init__(self, argv):
        # Core app that runs the GUI
        self.app = QApplication(argv)
        
        # Models
        

        # Subcontrollers
        #self.samplingTimerController = SamplingTimerController()

        # All Views
        self.mainGUI = MainGUI(self)

        # On initialization, show the Main GUI
        self.mainGUI.show()

        # Enable app, exit after window is closed
        sys.exit(self.app.exec_())

CoreController(sys.argv)