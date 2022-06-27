# PhotoLibraryController class, last edited 6/27/2022
import sys
from os.path import exists
from PyQt5 import QtWidgets as QtW
from PhotoLibrary.Photo import *
from PhotoLibrary.PhotoLibraryModel import *

class PhotoLibraryController:
    # Creates the models
    def __init__(self):
        # Views handled by core controller
        # Models
        self.photoLibrary = PhotoLibraryModel()
        # For now, read from default file, eventually add config files to change
        self.json = "Files/photolibrary.json"
        self.photoLibrary.readJSON(self.json)

        # Subcontrollers
        #self.samplingTimerController = SamplingTimerController()

    def updateJSON(self):
        self.photoLibrary.writeJSON(self.json)

    def convertTags(self, tags):
        checked = []
        for tag in tags:
            if tag.isChecked():
                checked += [tag.text()]
        return checked

    def addPhoto(self, location, tags):
        # Not a valid file, fail to add
        if not exists(location) or (".jpg" not in location and ".png" not in location):
            return False

        checked = self.convertTags(tags)

        self.photoLibrary.addPhotos([Photo(location, checked)])
        return True
