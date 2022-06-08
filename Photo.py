# Photo class, last edited 6/8/2022

class Photo:
    def __init__(self, fileLocation, photoTags):
        this.fileLocation = fileLocation
        this.photoTags = photoTags

    def addTags(self, tags):
        for tag in tags:
            if tag not in self.photoTags:
                self.photoTags += [tag]
