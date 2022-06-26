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

        backButton = QtW.QPushButton("Back", self.window)
        backButton.setGeometry(QtC.QRect(100,400,131,40))
        backButton.clicked.connect(self.mainView)



    # List of connected views
    def mainView(self):
        self.hide()

    # Use GUI to allow for adding photos
    def addPhotoDialog(self):
        addPhotoGUI = GUI(None, 800, 600, "Add a photo")

        linkText = QtW.QTextEdit("Photo Directory", addPhotoGUI.window)
        linkText.setGeometry(QtC.QRect(100,50,200,25))

        addButton = QtW.QPushButton("Back", addPhotoGUI.window)
        addButton.setGeometry(QtC.QRect(100,100,131,40))
        addButton.clicked.connect(lambda : addPhotoGUI.window.hide())

        backButton = QtW.QPushButton("Back", addPhotoGUI.window)
        backButton.setGeometry(QtC.QRect(100,100,131,40))
        backButton.clicked.connect(lambda : addPhotoGUI.window.hide())

        addPhotoGUI.show()

    # Access to backend functionality
    def requestAddPhoto(self):
        pass#self.controller.coreAddPhoto()
