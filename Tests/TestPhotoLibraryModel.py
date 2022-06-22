# Tests for PhotoLibraryModel class, last edited 6/10/2022
from os import getcwd
from Tests.Test import *
import PhotoLibrary.PhotoLibraryModel as photoLibraryModel
import PhotoLibrary.Photo as photo

def testAdd():
    swText("Adding photos to Library")
    
    library = photoLibraryModel.PhotoLibraryModel()

    ok = assertEquals("Initial", "Library", "Photos", [], library.getPhotos())

    list1 = [ "Happy", "Excited", "High BPM" ]
    list2 = [ "Sad", "Low BPM" ]
    list3 = [ "Calm", "Relaxed", "Medium BPM" ]

    photos = [photo.Photo("photo1.jpg", list1), photo.Photo("photo2.jpg", list2), photo.Photo("photo3.jpg", list3)]
    library.addPhotos(photos)

    ok = assertEquals("Added", "Library", "Photos", photos, library.getPhotos()) and ok

    swText(f"{'Test Passed' if ok else 'Test Failed. Quitting...'}")

    del library

    return ok

def testRemove():
    swText("Removing photos from Library")
    
    list1 = [ "Happy", "Excited", "High BPM" ]
    list2 = [ "Sad", "Low BPM" ]
    list3 = [ "Calm", "Relaxed", "Medium BPM" ]

    photos = [photo.Photo("photo1.jpg", list1), photo.Photo("photo2.jpg", list2), photo.Photo("photo3.jpg", list3)]

    library = photoLibraryModel.PhotoLibraryModel(photos)

    ok = assertEquals("Initial", "Library", "Photos", photos, library.getPhotos())

    library.clearPhotos()

    ok = assertEquals("Cleared", "Library", "Photos", [], library.getPhotos()) and ok

    library.addPhotos(photos)

    ok = assertEquals("Added", "Library", "Photos", photos, library.getPhotos()) and ok

    library.removePhotos(photos[0:2])
    photos = [photos[2]]

    ok = assertEquals("Remaining", "Library", "Photos", photos, library.getPhotos()) and ok

    swText(f"{'Test Passed' if ok else 'Test Failed. Quitting...'}")

    del library

    return ok

def testRead():
    swText("Reading from File")
    
    library = photoLibraryModel.PhotoLibraryModel()

    ok = assertEquals("Initial", "Library", "Photos", [], library.getPhotos())

    location = "Tests/testread.json"
    library.readJSON(location)

    list1 = [ "Happy", "Excited", "High BPM" ]
    list2 = [ "Sad", "Low BPM" ]
    list3 = [ "Calm", "Relaxed", "Medium BPM" ]

    photos = [photo.Photo("photo1.jpg", list1), photo.Photo("photo2.jpg", list2), photo.Photo("photo3.jpg", list3)]

    ok = assertEquals("New", "Library", "Photos", photos, library.getPhotos()) and ok

    swText(f"{'Test Passed' if ok else 'Test Failed. Quitting...'}")

    del library

    return ok
    
def testWrite():
    swText("Writing to File")

    # Create photos list
    list1 = [ "Happy", "Excited", "High BPM" ]
    list2 = [ "Sad", "Low BPM" ]
    list3 = [ "Calm", "Relaxed", "Medium BPM" ]

    photos = [photo.Photo("photo1.jpg", list1), photo.Photo("photo2.jpg", list2), photo.Photo("photo3.jpg", list3)]
    
    library = photoLibraryModel.PhotoLibraryModel(photos)

    ok = assertEquals("Initial", "Library", "Photos", photos, library.getPhotos())

    # Write photos to file
    location = "Tests/testwrite.json"
    library.writeJSON(location)

    # Clear library
    library.clearPhotos()

    ok = assertEquals("No", "Library", "Photos", [], library.getPhotos())

    # Read back into library
    library.readJSON(location)

    # Compare photos
    ok = assertEquals("Read", "Library", "Photos", photos, library.getPhotos()) and ok

    swText(f"{'Test Passed' if ok else 'Test Failed. Quitting...'}")

    # Clear file for next tests
    with open(location, "w") as file:
        file.truncate(0)

    del library

    return ok

def testEdit():
    pass

def runTests():
    header("Testing PhotoLibraryModel.py")

    if not testAdd():
        sys.exit()

    if not testRemove():
        sys.exit()

#    if not testEdit():
#        sys.exit()
        
    if not testRead():
       sys.exit()

    if not testWrite():
       sys.exit()

    header("Done testing PhotoLibraryModel.py")

if __name__ == "__main__":
    runTests()