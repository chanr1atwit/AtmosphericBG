# PhotoLibrary class, last edited 6/10/2022
import PhotoLibrary.Photo as photo
import json

class PhotoLibraryModel:
    # Create PhotoLibraryModel
    def __init__(self, photos=[]):
        self.__photos = photos

    # Read the stored library from json file
    def readJSON(self, jsonFile):
        with open(jsonFile, "r") as file:
            for item in json.load(file):
                self.__photos += [photo.Photo(item["location"], item["tags"])]                

    ### TESTING METHODS ###

    # Return the photo list
    def getPhotos(self):
        return self.__photos