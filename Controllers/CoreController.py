# CoreController class, last edited 6/20/2022
import sys
from PyQt5.QtWidgets import QApplication
from Views.MainGUI import *
from Views.PhotoLibraryGUI import *
from Views.SettingsGUI import *


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
        self.photoLibraryGUI = PhotoLibraryGUI(self)
        self.settingsGUI = SettingsGUI(self)

        # On initialization, show the Main GUI
        # If it closes, the app shuts down
        # Other windows will open as dialogs
        self.mainGUI.show()

        # Enable app, exit after window is closed
        sys.exit(self.app.exec_())

    def openView(self, view):
        view.show()
