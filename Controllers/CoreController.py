# CoreController class, last edited 6/27/2022
import sys
from PyQt5.QtWidgets import QApplication

from Controllers.PhotoLibraryController import *

from Views.MainGUI import *
from Views.PhotoLibraryGUI import *
from Views.SettingsGUI import *

class CoreController:
    # Create all elements of the app
    # Views, Controllers
    # Holds controller over what is shown
    def __init__(self, argv):
        # Core app that runs the GUI
        self.app = QApplication(argv)        

        # Subcontrollers
        self.photoLibraryController = PhotoLibraryController()
        #self.samplingTimerController = SamplingTimerController()

        # All Views
        self.mainGUI = MainGUI(self)
        self.photoLibraryGUI = PhotoLibraryGUI(self.photoLibraryController)
        self.settingsGUI = SettingsGUI(self)

        # On initialization, show the Main GUI
        # If it closes, the app shuts down
        # Other windows will open as dialogs
        self.mainGUI.show()

        # Enable app, exit after window is closed
        sys.exit(self.app.exec_())
