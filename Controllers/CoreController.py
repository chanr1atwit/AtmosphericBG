import sys, configparser

from PyQt5.QtWidgets import QApplication

from Controllers.PhotoLibraryController import *
from Controllers.DetectController import *
from Controllers.SamplingController import *

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
        self.config.read("Files/userconfig.ini")

        self.photoLibraryController = PhotoLibraryController(self)
        self.detectController = DetectController(self)
        self.samplingController = SamplingController(self)

        # Connected Views
        self.mainGUI = MainGUI(self)
        self.settingsGUI = SettingsGUI(self)

        # On initialization, show the Main GUI
        # If it closes, the app shuts down
        # Other windows will open as dialogs
        self.mainGUI.show()

        # Enable app, exit after window is closed
        sys.exit(self.app.exec_())

### Inter-controller functions
    def sendTags(self, tags):
        self.photoLibraryController.requestChangeBackground(tags)

### Configuration functions
    # Get configuration setting
    def getConfiguration(self, category, setting, confType):
        returnValue = None
        value = self.config[category][setting]
        if confType == bool:
            if value == "True":
                returnValue = True
            else:
                returnValue = False
        else:
            returnValue = confType(self.config[category][setting])
        return confType(returnValue)

    # Set configuration setting
    def setConfiguration(self, category, setting, value):
        self.config[category][setting] = str(value)

    # Write current configuration to file
    def writeConfiguration(self):
        with open("Files\\userconfig.ini", "w") as file:
            self.config.write(file)

### Settings GUI functions
    # Get enable state of PL
    def getPLState(self):
        return self.photoLibraryController.enablePL

    # Swap enable state of PL
    def setPLState(self, state):
        self.photoLibraryController.enablePL = state
        self.setConfiguration("PhotoLibrary", "library", state)

    # Get enable state of dyanmic generation
    def getDynamicState(self):
        return self.photoLibraryController.enableDynamic

    # Swap enable state of dyanmic generation
    def setDynamicState(self, state):
        self.photoLibraryController.enableDynamic = state
        self.setConfiguration("PhotoLibrary", "dynamic", state)
        print(f"{self.config['PhotoLibrary']['dynamic']}")

    # Set custom dimensions, check if valid
    def setCustomDims(self, width, height):
        dims = None
        # Valid dims
        if len(width) != 0  and len(height) != 0 and \
            int(width) > 99 and int(height) > 99:
            dims = [int(width), int(height)]
        self.photoLibraryController.customDims = dims

    # Get wait time from sampling timer
    def getWaitTime(self):
        return self.samplingController.waitTime

    # Set the wait time from user settings
    def setWaitTime(self, waitTime):
        self.samplingController.waitTime = waitTime

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
