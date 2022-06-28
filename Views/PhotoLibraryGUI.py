# MainGUI class, last edited 6/27/2022
from PyQt5 import QtCore as QtC
from PyQt5 import QtWidgets as QtW
from PyQt5 import QtGui as QtG
from Views.GUI import *

class PhotoLibraryGUI(GUI):
    # This function sets up the PhotoLibraryGUI view
    # NOTE: Uses a reference to the controller
    #       that created this View
    def __init__(self, controller):
        # Call to super init
        # Window and controller defined by GUI superclass
        super().__init__(controller, 1500, 800, "Atmospheric BG - Photo Library")
        self.num = 0




        listBox = QtW.QHBoxLayout(self.window)
        self.window.setLayout(listBox)

        scroll = QtW.QScrollArea(self.window)
        scroll.setGeometry(QtC.QRect(0, 0, 1300, 800))
        listBox.addWidget(scroll)
        scroll.setVerticalScrollBarPolicy(QtC.Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(QtC.Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        self.scrollContent = QtW.QWidget()
        self.scrollContent.setGeometry(QtC.QRect(0, 0, 1300, 800))

        scrollLayout = QtW.QVBoxLayout(self.scrollContent)

        vbox = QtW.QVBoxLayout(self.window)

        ## Holds reference to success/failure window
        ## so that the window doesn't immedeatly close.
        ## Will be set to none before each attempt at adding.
        #self.status = None

        

        #self.scroll = QtW.QScrollArea(self.window) # All pixmaps
        #self.scroll.setVerticalScrollBarPolicy(QtC.Qt.ScrollBarAlwaysOn)
        #self.scroll.setHorizontalScrollBarPolicy(QtC.Qt.ScrollBarAlwaysOff)
        #self.scroll.setWidgetResizable(True)
        #self.scroll.setWidget(self.widget)
        
        

        # HBox is stored in self.current
        # and number of images in self.num
        #self.addNewHBox() 
        #vLayout = QtG.QVBoxLayout()
        #vLayout.addWidget()
        #vLayout.addWidget(scroll)
        #self.setLayout(vLayout)

        # Buttons on View
        addButton = QtW.QPushButton("Add Photo", self.window)
        addButton.setGeometry(QtC.QRect(1320, 100, 131, 40))
        addButton.clicked.connect(self.addPhotoView)

        editButton = QtW.QPushButton("Edit Tags", self.window)
        editButton.setGeometry(QtC.QRect(1320, 200, 131, 40))
        editButton.clicked.connect(self.editTagsView)

        removeButton = QtW.QPushButton("Edit Tags", self.window)
        removeButton.setGeometry(QtC.QRect(1320, 300, 131, 40))
        removeButton.clicked.connect(self.controller.removePhoto)

        # Only here until save on close is implemented
        saveButton = QtW.QPushButton("Save Current Library", self.window)
        saveButton.setGeometry(QtC.QRect(1320, 400, 131, 40))
        saveButton.clicked.connect(self.controller.updateJSON)

        backButton = QtW.QPushButton("Back", self.window)
        backButton.setGeometry(QtC.QRect(1320,600,131,40))
        backButton.clicked.connect(self.mainView)




        vbox.addWidget(addButton)
        vbox.addWidget(editButton)
        vbox.addWidget(removeButton)
        vbox.addWidget(saveButton)
        vbox.addWidget(backButton)

        listBox.addChildLayout(vbox)
        scroll.setWidget(self.scrollContent)

    # List of connected views

    # Close current gui and return to main
    def mainView(self):
        self.controller.updateJSON()
        self.hide()

    # Use GUI to allow for adding photos
    def addPhotoView(self):
        addPhotoGUI = GUI(None, 600, 350, "Add a photo")

        linkText = QtW.QTextEdit("Photo Directory", addPhotoGUI.window)
        linkText.setGeometry(QtC.QRect(75,50,200,25))

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
        addButton.clicked.connect(lambda : self.controller.requestAddPhoto(addPhotoGUI, linkText, tags))

        browseButton = QtW.QPushButton("...", addPhotoGUI.window)
        browseButton.setGeometry(QtC.QRect(300, 50, 50, 25))
        browseButton.clicked.connect(lambda : self.controller.browseFiles(addPhotoGUI, linkText))

        backButton = QtW.QPushButton("Back", addPhotoGUI.window)
        backButton.setGeometry(QtC.QRect(400, 200, 131, 40))
        backButton.clicked.connect(lambda : addPhotoGUI.hide())

        addPhotoGUI.show()

    def editTagsView(self):
        pass

    def addPhotoSuccess(self):
        self.status = GUI(None, 200, 50, "Success!")
        success = QtW.QLabel("Successfully added photo!", self.status.window)
        success.setGeometry(QtC.QRect(0, 0, 200, 50))
        self.status.show()

    def addPhotoFailure(self):
        self.status = GUI(None, 200, 50, "Failure!")
        failure = QtW.QLabel("Failed to add photo.", self.status.window)
        failure.setGeometry(QtC.QRect(0, 0, 200, 50))
        self.status.show()

    #def addNewHBox(self):

    #    self.current = QtW.QHBoxLayout()
        
    #    self.images


    #    self.num = 0
