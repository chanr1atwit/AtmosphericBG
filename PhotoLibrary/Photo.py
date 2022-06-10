# Photo class, last edited 6/8/2022
class Photo:
    # Create a Photo with a location and optional tags
    # NOTE: Assumes that the location is valid and accessible,
    #       checking is done by the library itself
    def __init__(self, fileLocation, photoTags=[]):
        self.__fileLocation = fileLocation
        self.__photoTags = photoTags
    
    # Change the fileLocation of this Photo to the provided location
    # NOTE: Assumes that the location is valid and accessible,
    #       checking is done by the library itself
    def setLocation(self, location):
        self.__fileLocation = location
        
    # Reset(Empty) photoTags on this Photo
    # NOTE: Should be used when any tags are changed,
    #       followed by addTags
    def resetTags(self):
        self.__photoTags = []
    
    # Add a tag to photoTags
    def __addTag(self, tag):
        if tag not in self.__photoTags:
            self.__photoTags += [tag]

    # Add multiple tags to photoTags
    def addTags(self, tags):
        for tag in tags:
            self.__addTag(tag)

    ### TESTING METHODS ###

    # Return fileLocation
    def getLocation(self):
        return self.__fileLocation

    # Return photoTags
    def getTags(self):
        return self.__photoTags