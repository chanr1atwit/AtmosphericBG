import sys, configparser, random, threading

from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet

from Controllers.PhotoLibraryController import *
from Controllers.DetectController import *
from Controllers.SamplingController import *
from Controllers.LEDController import *

from Views.MainGUI import *
from Views.SettingsGUI import *
from Views.StartAudioGUI import *

import Visualizer.run_FFT_analyzer as visual

class CoreController:
    # Create all elements of the app
    # Views, Controllers
    # Holds controller over what is shown
    def __init__(self, argv):
        # Core app that runs the GUI
        self.app = QApplication(argv)

        self.config = configparser.ConfigParser()
        self.config.read("Files\\userconfig.ini")


        self.enableVisualizer = self.getConfiguration("Visualizer","enabled", bool)
        self.visualizer = visual.VisualizerObject(self.enableVisualizer)
        self.photoLibraryController = PhotoLibraryController(self)
        self.detectController = DetectController(self)
        self.samplingController = SamplingController(self)
        self.ledController = LEDController(self)

        # Connected Views
        self.mainGUI = MainGUI(self)
        self.settingsGUI = SettingsGUI(self)

        # Handle theme changing
        self.theme = self.getConfiguration("Settings", "theme", str)
        self.setTheme(self.theme)

        # On initialization, show the Main GUI
        # If it closes, the app shuts down
        # Other windows will open as dialogs
        self.mainGUI.show()

        # Enable app, exit after window is closed
        sys.exit(self.app.exec_())

### Inter-controller functions
    # Send tags from sampling timer to all controllers that need them
    def sendTags(self, tags):
        print(tags)
        self.photoLibraryController.requestChangeBackground(tags)
        self.setTheme(None, tags)

    # Reset background to before app was opened
    def resetBackground(self):
        self.photoLibraryController.updateBackground(
            self.photoLibraryController.background)

    def requestAnalysis(self):

        self.samplingController.requestPerformAnalysis()

    # Tell the sampling timer to shut down socket comms
    def requestClose(self):
        self.samplingController.requestClose()

    # Hide all GUIs so that app can shut down
    # Called from MainGUI, so exclude that one
    def hideAll(self):
        self.photoLibraryController.hideAll()
        self.settingsGUI.hide()
        self.detectController.hideAll()

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

    def setVisualizerState(self, state):
        self.enableVisualizer = state
        if self.enableVisualizer:
            self.visualizer.run()
        else:
            self.visualizer.stop()

    # Get the current theme
    def getTheme(self):
        return self.theme

    # Sets the current theme in configurations
    def setTheme(self, theme, tags=None):
        # Save the configuration if no tags
        # Non dynamic themes should always return here
        if tags is None and theme is not None:
            self.theme = theme
            self.setConfiguration("Settings", "theme", theme)
            apply_stylesheet(self.app, theme)
            return

        #theme = self.chooseTheme(tags)
        #print(theme)
        #apply_stylesheet(self.app, theme)
    
    # Choose a theme 
    def chooseTheme(self, tags):
        themes = ['default']

        if "Metal" in tags or "Rock" in tags:
            themes += ['dark_red.xml']
        if "Blues" in tags or "Country" in tags \
            or "Disco" in tags or "Jazz" in tags:
            themes += ['light_blue.xml']
        if "Classic" in tags or "Hip Hop" in tags \
            or "Pop" in tags or "Reggae" in tags:
            themes += ['light_teal.xml']
        return random.choice(themes)

    # Find the location of the LED app
    def findLEDProgram(self):
        self.ledController.findLEDProgram()

    # Open the LED app
    def runLEDApp(self):
        self.ledController.runLEDApp()

### List of connected views that need methods
    # Open Photo Library View
    def photoLibraryView(self):
        self.photoLibraryController.photoGUI.show()
        if self.ledController.path is not None:
            self.setConfiguration("Settings", "ledprogram", str(path))

    # Open Selection View
    def selectionView(self):
        self.detectController.audioGUI.show()

    # Open Settings View
    def settingsView(self):
        self.settingsGUI.show()
    