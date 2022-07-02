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

        listBox = QtW.QHBoxLayout(self)
        self.setLayout(listBox)

        scroll = QtW.QScrollArea(self)
        scroll.setGeometry(QtC.QRect(0, 0, 1300, 800))
        listBox.addWidget(scroll)
        scroll.setVerticalScrollBarPolicy(QtC.Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(QtC.Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        self.scrollContent = QtW.QWidget()
        self.scrollContent.setGeometry(QtC.QRect(0, 0, 1300, 800))

        scrollLayout = QtW.QVBoxLayout(self.scrollContent)

        vbox = QtW.QVBoxLayout(self)

        # Buttons on View
        addButton = QtW.QPushButton("Add Photo", self)
        addButton.setGeometry(QtC.QRect(1320, 100, 131, 40))
        addButton.clicked.connect(self.addPhotoView)

        editButton = QtW.QPushButton("Edit Tags", self)
        editButton.setGeometry(QtC.QRect(1320, 200, 131, 40))
        editButton.clicked.connect(self.editTagsView)

        removeButton = QtW.QPushButton("Remove Photo", self)
        removeButton.setGeometry(QtC.QRect(1320, 300, 131, 40))
        removeButton.clicked.connect(self.controller.requestRemovePhoto)

        # Only here until save on close is implemented
        saveButton = QtW.QPushButton("Save Current Library", self)
        saveButton.setGeometry(QtC.QRect(1320, 400, 131, 40))
        saveButton.clicked.connect(self.controller.updateJSON)

        backButton = QtW.QPushButton("Back", self)
        backButton.setGeometry(QtC.QRect(1320,600,131,40))
        backButton.clicked.connect(self.mainView)

        self.mood = QtW.QComboBox(self)
        self.mood.addItems(["Happy","Calm","Excited"])
        self.mood.setGeometry(QtC.QRect(1320,650,131,40))
        self.speed = QtW.QComboBox(self)
        self.speed.addItems(["Low","Medium","High"])
        self.speed.setGeometry(QtC.QRect(1320,700,131,40))

        changeButton = QtW.QPushButton("Change", self)
        changeButton.setGeometry(QtC.QRect(1320,750,131,40))
        changeButton.clicked.connect(lambda : self.controller.requestChangeBackground([self.mood.currentText(),self.speed.currentText()]))

        vbox.addWidget(addButton)
        vbox.addWidget(editButton)
        vbox.addWidget(removeButton)
        vbox.addWidget(saveButton)
        vbox.addWidget(backButton)
        vbox.addWidget(self.mood)
        vbox.addWidget(self.speed)
        vbox.addWidget(changeButton)


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

        linkText = QtW.QTextEdit("Photo Directory", addPhotoGUI)
        linkText.setGeometry(QtC.QRect(75,50,200,25))

        happy = QtW.QCheckBox("Happy", addPhotoGUI)
        happy.setGeometry(QtC.QRect(75, 100, 111, 20))
        sad = QtW.QCheckBox("Sad", addPhotoGUI)
        sad.setGeometry(QtC.QRect(75, 130, 111, 20))
        excited = QtW.QCheckBox("Excited", addPhotoGUI)
        excited.setGeometry(QtC.QRect(75, 160, 111, 20))
        calm = QtW.QCheckBox("Calm", addPhotoGUI)
        calm.setGeometry(QtC.QRect(75, 190, 111, 20))
        relaxed = QtW.QCheckBox("Relaxed", addPhotoGUI)
        relaxed.setGeometry(QtC.QRect(75, 220, 111, 20))
        low = QtW.QCheckBox("Low", addPhotoGUI)
        low.setGeometry(QtC.QRect(75, 250, 111, 20))
        medium = QtW.QCheckBox("Medium", addPhotoGUI)
        medium.setGeometry(QtC.QRect(75, 280, 111, 20))
        high = QtW.QCheckBox("High", addPhotoGUI)
        high.setGeometry(QtC.QRect(75, 310, 111, 20))

        tags = [happy, sad, excited, calm, relaxed, low, medium, high]

        addButton = QtW.QPushButton("Add", addPhotoGUI)
        addButton.setGeometry(QtC.QRect(400, 100, 131, 40))
        addButton.clicked.connect(lambda : self.controller.requestAddPhoto(addPhotoGUI, linkText, tags))

        browseButton = QtW.QPushButton("...", addPhotoGUI)
        browseButton.setGeometry(QtC.QRect(300, 50, 50, 25))
        browseButton.clicked.connect(lambda : self.controller.browseFiles(addPhotoGUI, linkText))

        backButton = QtW.QPushButton("Back", addPhotoGUI)
        backButton.setGeometry(QtC.QRect(400, 200, 131, 40))
        backButton.clicked.connect(lambda : addPhotoGUI.hide())

        addPhotoGUI.show()

    def editTagsView(self):
        if self.controller.findPhoto(self.controller.selected) is None:
            return

        editTagsGUI = GUI(None, 600, 350, "Edit tags")

        pTags = self.controller.getTags()

        happy = QtW.QCheckBox("Happy", editTagsGUI)
        happy.setGeometry(QtC.QRect(75, 100, 111, 20))
        happy.setChecked("Happy" in pTags)

        sad = QtW.QCheckBox("Sad", editTagsGUI)
        sad.setGeometry(QtC.QRect(75, 130, 111, 20))
        sad.setChecked("Sad" in pTags)
        
        excited = QtW.QCheckBox("Excited", editTagsGUI)
        excited.setGeometry(QtC.QRect(75, 160, 111, 20))
        excited.setChecked("Excited" in pTags)
        
        calm = QtW.QCheckBox("Calm", editTagsGUI)
        calm.setGeometry(QtC.QRect(75, 190, 111, 20))
        calm.setChecked("Calm" in pTags)
        
        relaxed = QtW.QCheckBox("Relaxed", editTagsGUI)
        relaxed.setGeometry(QtC.QRect(75, 220, 111, 20))
        relaxed.setChecked("Relaxed" in pTags)
        
        low = QtW.QCheckBox("Low", editTagsGUI)
        low.setGeometry(QtC.QRect(75, 250, 111, 20))
        low.setChecked("Low" in pTags)
        
        medium = QtW.QCheckBox("Medium", editTagsGUI)
        medium.setGeometry(QtC.QRect(75, 280, 111, 20))
        medium.setChecked("Medium" in pTags)

        high = QtW.QCheckBox("High", editTagsGUI)
        high.setGeometry(QtC.QRect(75, 310, 111, 20))
        high.setChecked("High" in pTags)

        tags = [happy, sad, excited, calm, relaxed, low, medium, high]

        editButton = QtW.QPushButton("Edit", editTagsGUI)
        editButton.setGeometry(QtC.QRect(400, 100, 131, 40))
        editButton.clicked.connect(lambda : self.controller.requestEditTags(editTagsGUI, tags))

        backButton = QtW.QPushButton("Back", editTagsGUI)
        backButton.setGeometry(QtC.QRect(400, 200, 131, 40))
        backButton.clicked.connect(lambda : editTagsGUI.hide())

        editTagsGUI.show()

    def success(self, text):
        self.status = GUI(None, 200, 50, "Success!")
        success = QtW.QLabel(f"Successfully {text}!", self.status)
        success.setGeometry(QtC.QRect(0, 0, 200, 50))
        self.status.show()

    def failure(self, text):
        self.status = GUI(None, 200, 50, "Failure!")
        failure = QtW.QLabel(f"Failed to {text}.", self.status)
        failure.setGeometry(QtC.QRect(0, 0, 200, 50))
        self.status.show()
