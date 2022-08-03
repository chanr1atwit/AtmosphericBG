import subprocess

import PyQt5.QtWidgets as QtW
import PyQt5.QtCore as QtC

class LEDController:
    def __init__(self, core):
        # Reference to core controller
        self.core = core
                
        path = self.core.getConfiguration("Settings", "ledprogram", str)
        if path is not None and path != "":
            self.path = path
        else:
            self.path = None

    # Assign the path to the LED program
    def findLEDProgram(self):
        try:
            # Browse for an application
            path = QtW.QFileDialog.getOpenFileName(self.core.settingsGUI, 'Open a program', QtC.QDir.rootPath(), '*.exe')

            # Check if application found
            if str(path[0]) == "":
                return

            # Assign the path
            self.path = str(path[0])

        # Possible error from OS
        except Exception as e:
            print(e)

    def runLEDApp(self):
        if self.path is None or self.path == "":
            return
        subprocess.run([self.path])
       
