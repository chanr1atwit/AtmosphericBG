# PhotoLibrary class, last edited 6/10/2022
import PhotoLibrary.Photo as photo
from json import load, dump, JSONEncoder
from os.path import exists

class PhotoLibraryModel:
    # Create PhotoLibraryModel
    def __init__(self, photos=[]):
        self.photos = list(photos)

    # Read the stored library from json file
    def readJSON(self, jsonFile):
        with open(jsonFile, "r") as file:
            for item in load(file):
                if not exists(item["location"]) or (".jpg" not in item["location"] and ".png" not in item["location"]):
                    continue
                self.photos += [photo.Photo(item["location"], item["tags"])]                

    # Write the stored library to json file
    def writeJSON(self, jsonFile):
        with open(jsonFile, "w") as file:
            dump(self.photos, file, cls=photo.PhotoEncoder)

    # Adds photo to current library
    # NOTE: Will not add duplicate photos
    def __addPhoto(self, item):
        if item not in self.photos:
            self.photos += [item]

    # Adds list of photos to current library
    def addPhotos(self, photos):
        for item in photos:
            self.__addPhoto(item)

    # Remove a photo from the library
    def removePhoto(self, item):
        if item in self.photos:
            self.photos.remove(item)

    # Remove the listed photos from the library
    def removePhotos(self, photos):
        for item in photos:
            self.removePhoto(item)

    # Clear the currently stored library
    def clearPhotos(self):
        self.photos = []

    # Return the photo list
    def getPhotos(self):
        return self.photos
