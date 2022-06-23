# MainGUI class, last edited 6/23/2022
from PyQt5 import QtCore as QtC
from PyQt5 import QtWidgets as QtW
from Views.GUI import *

class PhotoLibraryGUI(GUI):
    # This function sets up the PhotoLibraryGUI view
    # NOTE: Uses a reference to the controller
    #       that created this View
    def __init__(self, controller):
        # Call to super init
        # Window and controller defined by GUI superclass
        super().__init__(controller, 1500, 800, "Atmospheric BG - Photo Library")

        # Buttons on View
        addButton = QtW.QPushButton("Add Photo", self.window)
        addButton.setGeometry(QtC.QRect(100, 100, 131, 40))
        addButton.clicked.connect(self.addPhotoDialog)

        mainButton = QtW.QPushButton("Back", self.window)
        mainButton.setGeometry(QtC.QRect(100,400,131,40))
        mainButton.clicked.connect(self.mainView)



    # List of connected views
    def mainView(self):
        self.hide()

    def generateNewDialog(self):
        dialog = GUI(None, 300, 200, "Add a photo")
        return dialog

    def addPhotoDialog(self):
        dialog = self.generateNewDialog()
        dialog.show()

    # Access to backend functionality
    def requestAddPhoto(self):
        pass#self.controller.coreAddPhoto()
