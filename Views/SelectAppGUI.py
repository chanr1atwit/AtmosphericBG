from PyQt5 import QtCore as QtC
from PyQt5 import QtWidgets as QtW
from PyQt5.QtWidgets import QLineEdit
import threading
from Views.GUI import *

class SelectAppGUI(GUI):
    #remember to add controller back
    def __init__(self, controller):
        # Access to controller functions that do the work
        super().__init__(controller, 1500, 800, "Atmospheric BG - App Selection")

        addButton = QtW.QPushButton("Add New Source App", self)
        addButton.setGeometry(QtC.QRect(175, 100, 131, 40))   
        addButton.clicked.connect(self.AddNew)          
        
        backButton = QtW.QPushButton("Back", self)
        backButton.setGeometry(QtC.QRect(175,200,131,40))
        backButton.clicked.connect(self.mainView)
        
    def AddNew(self):
        textGUI = GUI(None, 200, 200,"Add New Source")
        textbox = QLineEdit(textGUI)
        textbox.setGeometry(QtC.QRect(0, 0, 200, 50))
        textGUI.show()
        self.controller.execList.add(textbox.text)
    

    def show(self):
        super().show()
        threading.Thread(target = self.controller.detectSources)
        print("displaying sources")
        
     # List of connected views
    def mainView(self):
        self.hide()

    # def displaySources(self):
    #     arr = self.controller.detectSources()
    #     i = 300
    #     for app in arr:
    #         button = QtW.QPushButton(app.Name, self)  
    #         button.setGeometry(175,i,131,40)          
    #         button.clicked.connect(self.selectSource(app.processID))
    #         i += 50

class ProcessButton(QtW.QPushButton):
    def __init__(self,process,parent = None):
        super(). __init__(process.Name,parent)
        self.process = process
       

        
    
    
    
    


        
