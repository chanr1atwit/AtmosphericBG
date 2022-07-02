# CoreController class, last edited 6/27/2022
import sys
from PyQt5.QtWidgets import QApplication

from Controllers.PhotoLibraryController import *
from Controllers.DetectController import *

from Views.MainGUI import *
from Views.SettingsGUI import *
from Views.SelectAppGUI import *

class CoreController:
    # Create all elements of the app
    # Views, Controllers
    # Holds controller over what is shown
    def __init__(self, argv):
        # Core app that runs the GUI
        self.app = QApplication(argv)        

        # Subcontrollers
        self.photoLibraryController = PhotoLibraryController()
        self.detectController = DetectController()
        #self.samplingTimerController = SamplingTimerController()

        # All Views
        self.mainGUI = MainGUI(self)
        self.settingsGUI = SettingsGUI(self)

        # On initialization, show the Main GUI
        # If it closes, the app shuts down
        # Other windows will open as dialogs
        self.mainGUI.show()

        # Enable app, exit after window is closed
        sys.exit(self.app.exec_())

    # Window should never be 'hidden' 
    # unless it is minimized by user
    def hide(self):
        pass

    # List of connected views that need methods
    def photoLibraryView(self):
        self.photoLibraryController.photoGUI.show()

    def selectionView(self):
        self.detectController.appSelectGUI.show()

    def settingsView(self):
        # NEED TO UPDATE SETTINGS GUI TO A GUI SUBCLASS
        # ALSO NEED TO MAKE SETTINGS CONTROLLER TO HOLD SETTINGS GUI
        self.settingsGUI.show()