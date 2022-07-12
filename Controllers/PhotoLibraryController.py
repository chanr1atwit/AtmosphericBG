import sys
import ctypes
import random

from PyQt5 import QtWidgets as QtW

from PhotoLibrary.Photo import *
from PhotoLibrary.PhotoLibraryModel import *
from Views.PhotoLibraryGUI import *

class PhotoLibraryController:
    # Creates the models
    def __init__(self):
        # Views
        self.photoGUI = PhotoLibraryGUI(self)
        self.photoLabels = []
        self.selected = None
        self.num = 0

        # Models
        self.photoLibrary = PhotoLibraryModel()
        # For now, read from default file, eventually add config files to change
        self.json = "Files/photolibrary.json"
        self.photoLibrary.readJSON(self.json)

        # Create images on view
        for picture in self.photoLibrary.getPhotos():
            label = self.createPixmap(picture.getLocation())
            self.photoLabels += [label]

    def getChoices(self, tags):
        photos = self.photoLibrary.getPhotos()
        choices = []
        for photo in photos:
            pTags = photo.getTags()
            if tags[0] in pTags and tags[1] in pTags:
                choices.append(photo)
        return choices

    # Request to change the background
    def requestChangeBackground(self, tags):
        choices = self.getChoices(tags)
        if len(choices) == 0:
            return
        photo = random.choice(choices)
        self.updateBackground(photo.getLocation())

    # Redraw every label
    def redrawWindow(self):
        self.num = 0
        self.photoGUI.initializeWindow()
        links = []
        for label in self.photoLabels:
            links += [label.link]
        for link in links:
            self.createPixmap(link)

    # Create a new image to display on the PL GUI
    # NOTE: The new pixmap gets queued up to be displayed
    #       when the user closes the add window
    def createPixmap(self, link):
        if self.num == 5:
            self.num = 0
            self.photoGUI.addNewHBox()
        self.num += 1
        label = Image(link)
        label.setFixedSize(260, 260)
        label.setScaledContents(True)
        label.setPixmap(QtG.QPixmap(link))
        label.mousePressEvent = lambda e: self.setSelectedLabel(label)
        label.setStyleSheet("padding :30px")
        self.photoGUI.hBoxLayout.addWidget(label)
        return label

    # Write all photos to the json file
    def updateJSON(self):
        self.photoLibrary.writeJSON(self.json)

    # Change the desktop background
    def updateBackground(self, link):
        link = link.replace("/", "\\")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, link, 0)

    # Get tags from selected photo
    def getTags(self):
        return self.findPhoto(self.selected.link).getTags()

    # Convert the checkbox values into tags
    def convertTags(self, tags):
        checked = []
        for tag in tags:
            if tag.isChecked():
                checked += [tag.text()]
        return checked
    
    # Find the photo based off selected
    def findPhoto(self, text):
        print("initiate find")
        for photo in self.photoLibrary.getPhotos():
            if text == photo.getLocation():
                print("found photo")
                return photo
        return None

    # Return label of selected photo on gui
    def setSelectedLabel(self, label):
        if self.selected is not None:
            self.selected.setStyleSheet("padding :30px")
        label.setStyleSheet("border: 2px solid red; padding :28px")
        self.selected = label
        print(self.selected.link)

    # Try to add a photo to the model
    def addPhoto(self, location, tags, text):
        # Not a valid file, fail to add
        if not exists(location) or (".jpg" not in location and ".png" not in location):
            return False
        checked = self.convertTags(tags)
        photo = Photo(location, checked)
        label = self.createPixmap(text)
        print(f"link {label.link}, photo {photo.getLocation()}")
        self.photoLabels += [label]
        self.photoLibrary.addPhotos([photo])
        return True

    # Check if photo is selected and delete if so
    def removePhoto(self):
        if self.selected.link == None:
            return False
        photo = self.findPhoto(self.selected.link)
        if photo == None:
            return False
        self.photoLibrary.removePhotos([photo])
        self.photoLabels.remove(self.selected)
        self.redrawWindow()
        return True

    # Edit tags of request photo
    def editTags(self, tags):
        if self.selected.link == None:
            return False
        print(f"{self.selected.link}")
        photo = self.findPhoto(self.selected.link)
        if photo == None:
            return False
        tags = self.convertTags(tags)
        self.photoLibrary.editTags(photo, tags)
        return True

    # Request for photo to be added, alert user to outcome
    def requestAddPhoto(self, gui, link, tags):
        self.photoGUI.status = None
        text = link.toPlainText().lower()
        if self.addPhoto(text, tags, text):
            gui.hide()    
            self.photoGUI.success("added photo")
            self.photoLibrary.writeJSON(self.json)
        else:
            gui.hide()
            self.photoGUI.failure("add photo")

    # Request for photo tags to be altered
    def requestEditTags(self, gui, tags):
        self.photoGUI.status = None
        if self.editTags(tags):
            gui.hide()
            self.photoGUI.success("altered tags")
            self.photoLibrary.writeJSON(self.json)
        else:
            gui.hide()
            self.photoGUI.failure("alter tags")

    # Request for photo to be removed
    def requestRemovePhoto(self):
        self.photoGUI.status = None
        ## Object has already been collected
        #if self.findPhoto(self.selected.link) is None:
        #    return
        if self.removePhoto():
            self.photoGUI.success("removed photo")
            self.photoLibrary.writeJSON(self.json)
            # FORCE REDRAW IMAGES HERE
        else:
            self.photoGUI.failure("remove photo")

    # Browse files on system
    def browseFiles(self, gui, text):
        # Not putting this in the GUI file as it is so short
        file = QtW.QFileDialog.getOpenFileName(gui, 'Open file','C://',"Image files (*.jpg *.png)")
        if file[0] == "":
            return
        text.setText(str(file[0]))

class Image(QtW.QLabel):
    def __init__(self, link, parent=None):
        super(Image, self).__init__(parent=parent)
        self.link = link
