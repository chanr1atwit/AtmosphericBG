# PhotoLibrary class, last edited 6/10/2022
import PhotoLibrary.Photo as photo
from json import load, dump, JSONEncoder

class PhotoLibraryModel:
    # Create PhotoLibraryModel
    def __init__(self, photos=[]):
        self.__photos = list(photos)

    # Read the stored library from json file
    def readJSON(self, jsonFile):
        with open(jsonFile, "r") as file:
            for item in load(file):
                self.__photos += [photo.Photo(item["location"], item["tags"])]                

    # Write the stored library to json file
    def writeJSON(self, jsonFile):
        with open(jsonFile, "w") as file:
            dump(self.__photos, file, cls=photo.PhotoEncoder)

    # Adds photo to current library
    # NOTE: Will not add duplicate photos
    def __addPhoto(self, item):
        if item not in self.__photos:
            self.__photos += [item]

    # Adds list of photos to current library
    def addPhotos(self, photos):
        for item in photos:
            self.__addPhoto(item)

    # Remove a photo from the library
    def __removePhoto(self, item):
        if item in self.__photos:
            self.__photos.remove(item)

    # Remove the listed photos from the library
    def removePhotos(self, photos):
        for item in photos:
            self.__removePhoto(item)

    # Clear the currently stored library
    def clearPhotos(self):
        self.__photos = []

    ### TESTING METHODS ###

    # Return the photo list
    def getPhotos(self):
        return self.__photos
