# PhotoLibrary class, last edited 6/10/2022
from PhotoLibrary.Photo import *
from json import load, dump, JSONEncoder
from os.path import exists

class PhotoLibraryModel:
    # Create PhotoLibraryModel
    def __init__(self, photos=[]):
        self.photos = list(photos)

    # Read the stored library from json file
    def readJSON(self, jsonFile):
        with open(jsonFile, "r") as file:
            for photo in load(file):
                if not exists(photo["location"]) or (".jpg" not in photo["location"] and ".png" not in photo["location"]):
                    continue
                self.photos += [Photo(photo["location"], photo["tags"])]                

    # Write the stored library to json file
    def writeJSON(self, jsonFile):
        with open(jsonFile, "w") as file:
            dump(self.photos, file, cls=PhotoEncoder)

    # Adds photo to current library
    # NOTE: Will not add duplicate photos
    def __addPhoto(self, photo):
        if photo not in self.photos:
            self.photos += [photo]

    # Adds list of photos to current library
    def addPhotos(self, photos):
        for photo in photos:
            self.__addPhoto(photo)

    def editTags(self, photo, tags):
        photo.resetTags()
        photo.addTags(tags)

    # Remove a photo from the library
    def removePhoto(self, photo):
        if photo in self.photos:
            self.photos.remove(photo)

    # Remove the listed photos from the library
    def removePhotos(self, photos):
        for photo in photos:
            self.removePhoto(photo)

    # Clear the currently stored library
    def clearPhotos(self):
        self.photos = []

    # Return the photo list
    def getPhotos(self):
        return self.photos
