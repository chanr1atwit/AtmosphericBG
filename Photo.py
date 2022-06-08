# Photo class, last edited 6/8/2022
class Photo:
    # Create a Photo with a location and optional tags
    # NOTE: Assumes that the location is valid and accessible,
    #       checking is done by the library itself
    def __init__(self, fileLocation, photoTags=[]):
        self.fileLocation = fileLocation
        self.photoTags = photoTags
    
    # Change the fileLocation of this Photo to the provided location
    # NOTE: Assumes that the location is valid and accessible,
    #       checking is done by the library itself
    def changeLocation(self, location):
        self.fileLocation = location

    # Reset(Empty) photoTags on this Photo
    # NOTE: Should be used when any tags are changed,
    #       followed by addTags
    def resetTags(self):
        this.photoTags = []
    
    # Add a tag to photoTags
    # NOTE: Should never be called explicitly outside of Photo,
    #       use addTags instead
    def addTag(self, tag):
        if tag not in self.photoTags:
            self.photoTags += [tag]

    # Add multiple tags to photoTags
    def addTags(self, tags):
        for tag in tags:
            addTag(tag)
