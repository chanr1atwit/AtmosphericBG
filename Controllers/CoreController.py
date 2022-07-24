import sys, configparser
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
        
        self.config = configparser.ConfigParser()
        self.config.read("Files\\userconfig.ini")

        # Subcontrollers
        # Only using default settings for PLController atm,
        # will be using config files for setup soon though
        self.photoLibraryController = PhotoLibraryController()
        self.detectController = DetectController()
        #self.samplingTimerController = SamplingTimerController()

        # Connected Views
        self.mainGUI = MainGUI(self)
        self.settingsGUI = SettingsGUI(self)  

        # On initialization, show the Main GUI
        # If it closes, the app shuts down
        # Other windows will open as dialogs
        self.mainGUI.show()

        # Enable app, exit after window is closed
        sys.exit(self.app.exec_())

### Configuration functions
    # Get configuration setting
    def getConfiguration(self, category, setting):
        return self.config[category][setting]

    # Set configuration setting
    def setConfiguration(self, category, setting, value):
        self.config[category][setting] = value

    # Write current configuration to file
    def writeConfiguration(self):
        with open("Files\\userconfig.ini", "w") as file:
            self.config.write(file)

### Settings GUI functions
    # Get enable state of PL
    def getPLState(self):
        print(f"{self.photoLibraryController.enablePL}")
        return self.photoLibraryController.enablePL

    # Swap enable state of PL
    def setPLState(self, state):
        self.photoLibraryController.enablePL = state

    # Get enable state of dyanmic generation
    def getDynamicState(self):
        return self.photoLibraryController.enableDynamic

    # Swap enable state of dyanmic generation
    def setDynamicState(self, state):
        self.photoLibraryController.enableDynamic = state

### Function overrides
    # Actions on app closure
    def closeEvent(self, event):
        self.writeConfiguration()
        event.accept()

### List of connected views that need methods
    # Open Photo Library View
    def photoLibraryView(self):
        self.photoLibraryController.photoGUI.show()

    # Open Selection View
    def selectionView(self):
        self.detectController.appSelectGUI.show()

    # Open Settings View
    def settingsView(self):
        self.settingsGUI.show()