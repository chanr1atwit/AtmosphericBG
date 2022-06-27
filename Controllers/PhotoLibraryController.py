# PhotoLibraryController class, last edited 6/27/2022
import sys
import ctypes

from PyQt5 import QtWidgets as QtW

from PhotoLibrary.Photo import *
from PhotoLibrary.PhotoLibraryModel import *
from Views.PhotoLibraryGUI import *


class PhotoLibraryController:
    # Creates the models
    def __init__(self):
        # Views
        self.photoGUI = PhotoLibraryGUI(self)

        # Models
        self.photoLibrary = PhotoLibraryModel()
        # For now, read from default file, eventually add config files to change
        self.json = "Files/photolibrary.json"
        self.photoLibrary.readJSON(self.json)

        self.cx = 30
        self.cy = 50

        # Create images on view
        for picture in self.photoLibrary.getPhotos():
            self.createPixmap(picture.getLocation())

    # Create a new image to display on the PL GUI
    # NOTE: The new pixmap gets queued up to be displayed
    #       when the user closes the add window
    def createPixmap(self, link):
        if self.photoGUI.num == 5:
            self.cx = 30
            self.cy += 250
            self.photoGUI.num = 0
            #self.photoGUI.addNewHBox()
        self.photoGUI.num += 1
        label = QtW.QLabel(self.photoGUI.window)

        label.setFixedSize(200, 200)
        label.move(self.cx, self.cy)
        self.cx += 260
        label.setScaledContents(True)
        label.setPixmap(QtG.QPixmap(link))
        #label.setStyleSheet("padding :30px")

    # Write all photos to the json file
    def updateJSON(self):
        self.photoLibrary.writeJSON(self.json)

    # Change the desktop background
    def updateBackground(self, link):
        link = link.replace("/", "\\")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, link, 0)

    # Convert the checkbox values into tags
    def convertTags(self, tags):
        checked = []
        for tag in tags:
            if tag.isChecked():
                checked += [tag.text()]
        return checked

    # Try to add a photo to the model
    def addPhoto(self, location, tags):
        # Not a valid file, fail to add
        if not exists(location) or (".jpg" not in location and ".png" not in location):
            return False
        checked = self.convertTags(tags)
        self.photoLibrary.addPhotos([Photo(location, checked)])
        return True

    # Check if photo is selected and delete if so
    def removePhoto(self):
        pass

    # Request for photo to be added, alert user to outcome
    def requestAddPhoto(self, gui, link, tags):
        print(f"{self.cx}, {self.cy}")
        self.photoGUI.status = None
        text = link.toPlainText().lower()
        if self.addPhoto(text, tags):
            gui.hide()
            self.createPixmap(text)
            self.photoGUI.addPhotoSuccess()
            self.photoGUI.window.update()
        else:
            gui.hide()
            self.photoGUI.addPhotoFailure()

    # Browse files on system
    def browseFiles(self, gui, text):
        # Not putting this in the GUI file as it is so short
        file = QtW.QFileDialog.getOpenFileName(gui.window, 'Open file','C://',"Image files (*.jpg *.png)")
        if file[0] == "":
            return
        text.setText(str(file[0]))
