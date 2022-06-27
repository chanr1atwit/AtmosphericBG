# MainGUI class, last edited 6/26/2022
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
        # Holds reference to success/failure window
        # so that the window doesn't immedeatly close
        self.status = None
        self.text = ""

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
        addPhotoGUI = GUI(None, 800, 350, "Add a photo")

        self.text = QtW.QTextEdit("Photo Directory", addPhotoGUI.window)
        self.text.setGeometry(QtC.QRect(75,50,200,25))

        browseButton = QtW.QPushButton("...", addPhotoGUI.window)
        browseButton.setGeometry(QtC.QRect(300, 50, 50, 25))
        browseButton.clicked.connect(lambda : self.browseFiles(self.text))

        #add elipse button next to linkText

        happy = QtW.QCheckBox("Happy", addPhotoGUI.window)
        happy.setGeometry(QtC.QRect(75, 100, 111, 20))

        sad = QtW.QCheckBox("Sad", addPhotoGUI.window)
        sad.setGeometry(QtC.QRect(75, 130, 111, 20))
        
        excited = QtW.QCheckBox("Excited", addPhotoGUI.window)
        excited.setGeometry(QtC.QRect(75, 160, 111, 20))
        
        calm = QtW.QCheckBox("Calm", addPhotoGUI.window)
        calm.setGeometry(QtC.QRect(75, 190, 111, 20))
        
        relaxed = QtW.QCheckBox("Relaxed", addPhotoGUI.window)
        relaxed.setGeometry(QtC.QRect(75, 220, 111, 20))
        
        low = QtW.QCheckBox("Low", addPhotoGUI.window)
        low.setGeometry(QtC.QRect(75, 250, 111, 20))

        medium = QtW.QCheckBox("Medium", addPhotoGUI.window)
        medium.setGeometry(QtC.QRect(75, 280, 111, 20))

        high = QtW.QCheckBox("High", addPhotoGUI.window)
        high.setGeometry(QtC.QRect(75, 310, 111, 20))

        tags = [happy, sad, excited, calm, relaxed, low, medium, high]

        addButton = QtW.QPushButton("Add", addPhotoGUI.window)
        addButton.setGeometry(QtC.QRect(400, 100, 131, 40))
        addButton.clicked.connect(lambda : self.requestAddPhoto(addPhotoGUI, linkText, tags))

        backButton = QtW.QPushButton("Back", addPhotoGUI.window)
        backButton.setGeometry(QtC.QRect(400, 200, 131, 40))
        backButton.clicked.connect(lambda : addPhotoGUI.window.hide())

        addPhotoGUI.show()

    def addPhotoSuccess(self):
        self.status = GUI(None, 200, 50, "Success!")
        success = QtW.QLabel("Successfully added photo!", self.status.window)
        success.setGeometry(QtC.QRect(0, 0, 200, 50))
        self.status.window.show()

    def addPhotoFailure(self):
        self.status = GUI(None, 200, 50, "Failure!")
        failure = QtW.QLabel("Failed to add photo.", self.status.window)
        failure.setGeometry(QtC.QRect(0, 0, 200, 50))
        self.status.window.show()

    # Access to backend functionality
    def requestAddPhoto(self, gui, link, tags):
        self.status = None
        if self.controller.addPhoto(link, tags):
            self.addPhotoSuccess()
        else:
            self.addPhotoFailure()
    
    def browseFiles(self, text):
        temp = GUI(None, 500, 500, "Open File").window
        file = QtW.QFileDialog.getOpenFileName(temp, 'Open file','C:\\',"Image files (*.jpg *.png)")
        if file[0] == "":
            return
        self.text.setText(file[0])
