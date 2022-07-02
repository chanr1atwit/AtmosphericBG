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

        self.hBoxLayout = None

        self.initializeWindow()

    def createButtons(self):

        vBoxWidget = QtW.QWidget()

        vBox = QtW.QVBoxLayout(vBoxWidget)

        # Buttons on View
        addButton = QtW.QPushButton("Add Photo")
        addButton.clicked.connect(self.addPhotoView)
        addButton.resize(131,60)

        editButton = QtW.QPushButton("Edit Tags")
        editButton.clicked.connect(self.editTagsView)
        editButton.resize(131,60)


        removeButton = QtW.QPushButton("Remove Photo")
        removeButton.clicked.connect(self.controller.requestRemovePhoto)
        removeButton.resize(131,60)

        # Only here until save on close is implemented
        saveButton = QtW.QPushButton("Save Current Library")
        saveButton.clicked.connect(self.controller.updateJSON)
        saveButton.resize(131,60)

        backButton = QtW.QPushButton("Back")
        backButton.clicked.connect(self.mainView)
        backButton.resize(131,60)


        mood = QtW.QComboBox()
        mood.addItems(["Happy","Calm","Excited"])
        mood.resize(131,60)
        speed = QtW.QComboBox()
        speed.addItems(["Low","Medium","High"])
        speed.resize(131,60)

        changeButton = QtW.QPushButton("Change")
        changeButton.clicked.connect(lambda : self.controller.requestChangeBackground([mood.currentText(),speed.currentText()]))
        changeButton.resize(131,60)

        vBox.addWidget(addButton)
        vBox.addWidget(editButton)
        vBox.addWidget(removeButton)
        vBox.addWidget(saveButton)
        vBox.addWidget(backButton)
        vBox.addWidget(mood)
        vBox.addWidget(speed)
        vBox.addWidget(changeButton)

        return vBoxWidget

    def addNewHBox(self):
        hBoxWidget = QtW.QWidget()
        self.hBoxLayout = QtW.QHBoxLayout(hBoxWidget)
        self.scrollLayout.addWidget(hBoxWidget)
        print(f"{str(self.hBoxLayout)}")

    def initializeWindow(self):
        self.controller.selected = None
        self.scrollLayout = None
        self.hBoxLayout = None
        self.setCentralWidget(None)


        # HBox that holds all widgets
        window = QtW.QWidget()
        window.setGeometry(QtC.QRect(0, 0, 1500, 800))
        mainHBox = QtW.QHBoxLayout(window)

        # Set window to main widget
        self.setCentralWidget(window)

        # Create the widget which will scroll
        scrollWidget = QtW.QWidget()
        scrollWidget.setGeometry(QtC.QRect(0, 0, 1300, 800))

        scrollArea = QtW.QScrollArea()
        scrollArea.setGeometry(QtC.QRect(0, 0, 1300, 800))
        scrollArea.setHorizontalScrollBarPolicy(QtC.Qt.ScrollBarAlwaysOff)
        scrollArea.setWidgetResizable(True)        
        scrollArea.setWidget(scrollWidget)

        # Layout for scrollWidget, which is scrollable
        self.scrollLayout = QtW.QVBoxLayout(scrollWidget)

        buttons = self.createButtons()

        self.addNewHBox()

        mainHBox.addWidget(scrollArea)
        mainHBox.addWidget(buttons)

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
