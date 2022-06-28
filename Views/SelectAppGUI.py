from Controllers import DetectController
from PyQt5 import QtCore as QtC
from PyQt5 import QtWidgets as QtW
from Views.GUI import *
class SelectAppGUI:
    #remember to add controller back
    def __init__(self):
        # Access to controller functions that do the work
        #super().__init__(controller, 1500, 800, "Atmospheric BG - App Selection")

        #temporary window
        self.window = QtW.QMainWindow()
        self.window.setGeometry(0, 0, 500, 500)
        self.window.setWindowTitle("Atmospheric BG - App Selection")
        self.window.setWindowModality(QtC.Qt.ApplicationModal)
    
        addButton = QtW.QPushButton("New App", self.window)
        addButton.setGeometry(QtC.QRect(175, 100, 131, 40))

        #arr = controller.detectSources()
        #for each application, make new button
        #for app in arr:
            #addSelection = QtW.QPushButton(str(app), self.window)
            #addSelection.setGeometry(QtC.QRect(100, 100, 131, 40))
        
        backButton = QtW.QPushButton("Back", self.window)
        backButton.setGeometry(QtC.QRect(175,200,131,40))
        backButton.clicked.connect(self.mainView)

         
    def show(self):
        self.window.show()

    def hide(self):
        self.window.hide()

    # List of connected views
    def mainView(self):
        self.hide()


        
