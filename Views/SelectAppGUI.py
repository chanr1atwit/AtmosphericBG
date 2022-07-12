from PyQt5 import QtCore as QtC
from PyQt5 import QtWidgets as QtW

from Views.GUI import *

class SelectAppGUI(GUI):
    #remember to add controller back
    def __init__(self, controller):
        # Access to controller functions that do the work
        super().__init__(controller, 1500, 800, "Atmospheric BG - App Selection")

        addButton = QtW.QPushButton("Add New Soure App", self)
        addButton.setGeometry(QtC.QRect(175, 100, 131, 40))             
        
        backButton = QtW.QPushButton("Back", self)
        backButton.setGeometry(QtC.QRect(175,200,131,40))
        backButton.clicked.connect(self.mainView)
        
    def addnew():
        pass

    def show(self):
        print("displaing sources")
        self.displaySources()
        super().show()


    # List of connected views
    def mainView(self):
        self.hide()

    def displaySources(self):
        arr = self.controller.detectSources()
        i = 300
        #for each application, make new buttons(loop works!)
        for app in arr:
            button = QtW.QPushButton(app.Name, self)  
            button.setGeometry(175,i,131,40)          
            button.clicked.connect(self.mainView)
            i += 50
        
