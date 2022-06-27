# PhotoLibraryController class, last edited 6/26/2022
import sys
import os
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
        self.photoLibrary.readJSON("Files/photolibrary.json")

        # Subcontrollers
        #self.samplingTimerController = SamplingTimerController()
        
    def openView(self, view):
        view.show()

    def convertTags(tags):
        checked = []
        for tag in tags:
            if tag.isChecked():
                checked += [tag.text()]
        return checked

    def addPhoto(self, location, tags):
        # Not a valid file, fail to add
        if not exists(location) or (".jpg" not in location and ".png" not in location):
            return False

        checked = convertTags(tags)

        self.photoLibrary.addPhotos([Photo(location, checked)])
