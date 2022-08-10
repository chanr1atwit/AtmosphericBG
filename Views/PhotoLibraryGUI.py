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
        super().__init__(controller, 1600, 800, "Atmospheric BG - Photo Library")
        self.status = None

        self.hBoxLayout = None

        self.initializeWindow()

        self.addPhotoGUI = None

        self.editTagsGUI = None

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
        mood.addItems(["Blues","Classic","Country","Disco","Hip Hop","Jazz","Metal","Pop","Reggae","Rock"])
        mood.resize(131,60)

        changeButton = QtW.QPushButton("Change")
        changeButton.clicked.connect(lambda : self.controller.requestChangeBackground([mood.currentText()]))
        changeButton.resize(131,60)

        vBox.addWidget(addButton)
        vBox.addWidget(editButton)
        vBox.addWidget(removeButton)
        vBox.addWidget(saveButton)
        vBox.addWidget(backButton)
        vBox.addWidget(mood)
        vBox.addWidget(changeButton)

        return vBoxWidget

    def addNewHBox(self):
        hBoxWidget = QtW.QWidget()
        self.hBoxLayout = QtW.QHBoxLayout(hBoxWidget)
        self.scrollLayout.addWidget(hBoxWidget)
        self.hBoxLayout.setAlignment(QtC.Qt.AlignLeft)

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

### List of connected views
    # Close current gui and return to main
    def mainView(self):
        self.controller.updateJSON()
        self.hide()

    # Use GUI to allow for adding photos
    def addPhotoView(self):
        self.addPhotoGUI = GUI(None, 600, 400, "Add a photo")
        self.addPhotoGUI.setWindowModality(QtC.Qt.ApplicationModal)

        linkText = QtW.QTextEdit("Photo Directory", self.addPhotoGUI)
        linkText.setGeometry(QtC.QRect(75,50,400,25))

        blues = QtW.QCheckBox("Blues", self.addPhotoGUI)
        blues.setGeometry(QtC.QRect(75, 100, 111, 20))
        classic = QtW.QCheckBox("Classic", self.addPhotoGUI)
        classic.setGeometry(QtC.QRect(75, 130, 111, 20))
        country = QtW.QCheckBox("Country", self.addPhotoGUI)
        country.setGeometry(QtC.QRect(75, 160, 111, 20))
        disco = QtW.QCheckBox("Disco", self.addPhotoGUI)
        disco.setGeometry(QtC.QRect(75, 190, 111, 20))
        hiphop = QtW.QCheckBox("Hip Hop", self.addPhotoGUI)
        hiphop.setGeometry(QtC.QRect(75, 220, 111, 20))
        jazz = QtW.QCheckBox("Jazz", self.addPhotoGUI)
        jazz.setGeometry(QtC.QRect(75, 250, 111, 20))
        metal = QtW.QCheckBox("Metal", self.addPhotoGUI)
        metal.setGeometry(QtC.QRect(75, 280, 111, 20))
        pop = QtW.QCheckBox("Pop", self.addPhotoGUI)
        pop.setGeometry(QtC.QRect(75, 310, 111, 20))
        reggae = QtW.QCheckBox("Reggae", self.addPhotoGUI)
        reggae.setGeometry(QtC.QRect(75, 340, 111, 20))
        rock = QtW.QCheckBox("Rock", self.addPhotoGUI)
        rock.setGeometry(QtC.QRect(75, 370, 111, 20))


        tags = [blues, classic, country, disco, hiphop, jazz, metal, pop, reggae, rock]

        addButton = QtW.QPushButton("Add", self.addPhotoGUI)
        addButton.setGeometry(QtC.QRect(400, 100, 131, 40))
        addButton.clicked.connect(lambda : self.controller.requestAddPhoto(self.addPhotoGUI, linkText, tags))

        browseButton = QtW.QPushButton("...", self.addPhotoGUI)
        browseButton.setGeometry(QtC.QRect(480, 50, 50, 25))
        browseButton.clicked.connect(lambda : self.controller.browseFiles(self.addPhotoGUI, linkText))

        backButton = QtW.QPushButton("Back", self.addPhotoGUI)
        backButton.setGeometry(QtC.QRect(400, 200, 131, 40))
        backButton.clicked.connect(lambda : self.addPhotoGUI.hide())

        self.addPhotoGUI.show()

    # Open the edit tags view
    def editTagsView(self):
        if self.controller.selected is None or \
           self.controller.selected.link is None or \
           self.controller.findPhoto(self.controller.selected.link) is None:
            return

        self.editTagsGUI = GUI(None, 600, 400, "Edit tags")
        self.editTagsGUI.setWindowModality(QtC.Qt.ApplicationModal)

        pTags = self.controller.getTags()

        blues = QtW.QCheckBox("Blues", self.editTagsGUI)
        blues.setGeometry(QtC.QRect(75, 100, 111, 20))
        blues.setChecked("Blues" in pTags)
        classic = QtW.QCheckBox("Classic", self.editTagsGUI)
        classic.setGeometry(QtC.QRect(75, 130, 111, 20))
        classic.setChecked("Classic" in pTags)
        country = QtW.QCheckBox("Country", self.editTagsGUI)
        country.setGeometry(QtC.QRect(75, 160, 111, 20))
        country.setChecked("Country" in pTags)
        disco = QtW.QCheckBox("Disco", self.editTagsGUI)
        disco.setGeometry(QtC.QRect(75, 190, 111, 20))
        disco.setChecked("Disco" in pTags)
        hiphop = QtW.QCheckBox("Hip Hop", self.editTagsGUI)
        hiphop.setGeometry(QtC.QRect(75, 220, 111, 20))
        hiphop.setChecked("Hip Hop" in pTags)
        jazz = QtW.QCheckBox("Jazz", self.editTagsGUI)
        jazz.setGeometry(QtC.QRect(75, 250, 111, 20))
        jazz.setChecked("Jazz" in pTags)
        metal = QtW.QCheckBox("Metal", self.editTagsGUI)
        metal.setGeometry(QtC.QRect(75, 280, 111, 20))
        metal.setChecked("Metal" in pTags)
        pop = QtW.QCheckBox("Pop", self.editTagsGUI)
        pop.setGeometry(QtC.QRect(75, 310, 111, 20))
        pop.setChecked("Pop" in pTags)
        reggae = QtW.QCheckBox("Reggae", self.editTagsGUI)
        reggae.setGeometry(QtC.QRect(75, 340, 111, 20))
        reggae.setChecked("Reggae" in pTags)
        rock = QtW.QCheckBox("Rock", self.editTagsGUI)
        rock.setGeometry(QtC.QRect(75, 370, 111, 20))
        rock.setChecked("Rock" in pTags)

        tags = [blues, classic, country, disco, hiphop, jazz, metal, pop, reggae, rock]

        editButton = QtW.QPushButton("Edit", self.editTagsGUI)
        editButton.setGeometry(QtC.QRect(400, 100, 131, 40))
        editButton.clicked.connect(lambda : self.controller.requestEditTags(self.editTagsGUI, tags))

        backButton = QtW.QPushButton("Back", self.editTagsGUI)
        backButton.setGeometry(QtC.QRect(400, 200, 131, 40))
        backButton.clicked.connect(lambda : self.editTagsGUI.hide())

        self.editTagsGUI.show()

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

    def hide(self):
        if self.status is not None:
            self.status.close()
        if self.addPhotoGUI is not None:
            self.addPhotoGUI.hide()
        if self.editTagsGUI is not None:
            self.editTagsGUI.hide()
        super().hide()
