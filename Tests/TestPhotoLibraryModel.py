# Tests for PhotoLibraryModel class, last edited 6/10/2022
from os import getcwd
from Tests.Test import *
import PhotoLibrary.PhotoLibraryModel as photoLibraryModel
import PhotoLibrary.Photo as photo

# 'Default' values
def fillTags():
    return ["Happy", "Excited", "Medium BPM"]

def testRead():
    swText("Reading from File")
    
    library = photoLibraryModel.PhotoLibraryModel()

    ok = assertEquals("Initial", "Library", "Photos", [], library.getPhotos())

    print(f"{getcwd()}")

    location = "Tests/testread.json"
    library.readJSON(location)

    list1 = [ "Happy", "Excited", "High BPM" ]
    list2 = [ "Sad", "Low BPM" ]
    list3 = [ "Calm", "Relaxed", "Medium BPM" ]

    photos = [photo.Photo("photo1.jpg", list1), photo.Photo("photo2.jpg", list2), photo.Photo("photo3.jpg", list3)]

    ok = assertEquals("New", "Library", "Photos", photos, library.getPhotos()) and ok

    swText(f"{'Test Passed' if ok else 'Test Failed. Quitting...'}")

    return ok
    
def runTests():
    header("Testing PhotoLibraryModel.py")

    if not testRead():
       sys.exit()

    header("Done testing PhotoLibraryModel.py")

if __name__ == "__main__":
    runTests()