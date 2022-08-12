import sys
import ctypes
import random
import threading
import win32con
from os import remove, getcwd

from PyQt5 import QtWidgets as QtW

# DBG library handles all the functionality behind temporary backgrounds.
from PhotoLibrary import DynamicBackgroundGeneration as DBG
from PhotoLibrary.Photo import *
from PhotoLibrary.PhotoLibraryModel import *
from Views.PhotoLibraryGUI import *

class PhotoLibraryController:
    def __init__(self, core):
        # Core allows reads and writes to configurations
        self.core = core

        # Views
        self.photoGUI = PhotoLibraryGUI(self)
        self.photoLabels = []
        self.selected = None
        self.num = 0

        # If both are False, all PL user functionality is essentially disabled
        self.enableDynamic = self.core.getConfiguration("PhotoLibrary","dynamic", bool)
        self.enablePL = self.core.getConfiguration("PhotoLibrary", "library", bool)

        # When false, lock the sampling timer, photo is being generated
        self.finished = True
        self.background = self.getWallpaper()
        
        # Holds custom dims for image generation
        dims = [self.core.getConfiguration("Settings", "width", str),
                self.core.getConfiguration("Settings", "height", str)]
        if dims[0] != "" and dims[1] != "":
            dims[0] = int(dims[0])
            dims[1] = int(dims[1])
            self.customDims = dims
        else:
            self.customDims = None

        # Models
        self.photoLibrary = PhotoLibraryModel()
        # For now, read from default file, add file to settings gui later
        self.json = self.core.getConfiguration("PhotoLibrary", "file", str)
        self.photoLibrary.readJSON(self.json)

        # Create images on view
        for picture in self.photoLibrary.getPhotos():
            label = self.createPixmap(picture.getLocation())
            self.photoLabels += [label]
    # Hide all photo library related GUIs
    def hideAll(self):
        self.photoGUI.hide()

    def getChoices(self, tags):
        photos = []
        if self.enablePL:
            photos = self.photoLibrary.getPhotos()
        choices = []
        for photo in photos:
            pTags = photo.getTags()
            allIn = True
            for tag in tags:
                if tag not in pTags:
                    allIn = False
                    break
            if allIn:
                choices.append(photo)
        if self.enableDynamic:
            # Signal Photo that should be discarded after use
            choices.append(Photo("dynamic"))
        return choices

    # Request to change the background
    def requestChangeBackground(self, tags):
        choices = self.getChoices(tags)
        if len(choices) == 0:
            return
        photo = random.choice(choices)
        if photo.getLocation() == "dynamic":
            # Generate temporary background
            imageLocation = f"{getcwd()}\\TemporaryFiles\\photo.png"
            threading.Thread(target=self.generationTask, args=(tags, imageLocation, self.customDims,)).start()
        else:
            self.updateBackground(photo.getLocation())

    def getWallpaper(self):
        ubuf = ctypes.create_unicode_buffer(512)
        ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_GETDESKWALLPAPER,len(ubuf),ubuf,0)
        return ubuf.value

    # Generate image on a separate thread
    def generationTask(self, tags, imageLocation, dims):
        print("Generating new image...")
        # Generate new image
        DBG.generateImage(tags, imageLocation, dims)    
        # Update the background
        self.updateBackground(imageLocation) 
        print("Finished generating image")

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

    # Update to a new JSON file
    def updateLink(self, link):
        # Save the current JSON
        self.updateJSON()
        # Update configuration and link to new file
        self.json = link
        self.core.setConfiguration("PhotoLibrary", "file", self.json)
        # Clear the library
        self.photoLibrary.clearPhotos()
        self.photoLabels = []
        # Fill the library
        self.photoLibrary.readJSON(self.json)
        # Redraw the window
        self.redrawWindow()
        # Create images on view
        for picture in self.photoLibrary.getPhotos():
            label = self.createPixmap(picture.getLocation())
            self.photoLabels += [label]

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
        for photo in self.photoLibrary.getPhotos():
            if text == photo.getLocation():
                return photo
        return None

    # Return label of selected photo on gui
    def setSelectedLabel(self, label):
        if self.selected is not None:
            self.selected.setStyleSheet("padding :30px")
        label.setStyleSheet("border: 2px solid red; padding :28px")
        self.selected = label

    # Try to add a photo to the model
    def addPhoto(self, location, tags, text):
        # Not a valid file, fail to add
        if not exists(location) or (".jpg" not in location and ".png" not in location):
            return False
        checked = self.convertTags(tags)
        photo = Photo(location, checked)
        label = self.createPixmap(text)
        self.photoLabels += [label]
        self.photoLibrary.addPhotos([photo])
        return True

    # Check if photo is selected and delete if so
    def removePhoto(self):
        if self.selected is None or self.selected.link is None:
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
        fileName = QtW.QFileDialog.getOpenFileName(gui, 'Open file','C://',"Image files (*.jpg *.png)")
        if fileName[0] == "":
            return
        text.setText(str(fileName[0]))

class Image(QtW.QLabel):
    def __init__(self, link, parent=None):
        super(Image, self).__init__(parent=parent)
        self.link = link
