# Tests for Photo class, last edited 6/8/2022
from Tests.Test import *
import PhotoLibrary.Photo as photo

# 'Default' values
def fillTags():
    return ["Happy", "Excited", "Medium BPM"]

def testPhoto():
    swText("Creating Photo")
    location = "/files/tests/hello.jpg"
    tags = fillTags()

    photo1 = photo.Photo(location, tags)
    ok = assertEquals("Provided", "Photo", "Location", location, photo1.getLocation())
    ok = assertEquals("Provided", "Photo", "Tags", tags, photo1.getTags()) and ok

    swText(f"{'Test Passed' if ok else 'Test Failed. Quitting...'}")

    return ok

def testLocation():
    swText("Changing Location")
    location = "/files/tests/hello.jpg"
    photo1 = photo.Photo(location)
    ok = assertEquals("Initial", "Photo", "Location", location, photo1.getLocation())

    location = "/files/tests/goodbye.jpg"
    photo1.setLocation(location)
    ok = assertEquals("New", "Photo", "Location", location, photo1.getLocation()) and ok

    swText(f"{'Test Passed' if ok else 'Test Failed. Quitting...'}")

    return ok

def testResetTags():
    swText("Reset Tags")
    location = "/files/tests/hello.jpg"
    photo1 = photo.Photo(location, fillTags())
    ok = assertEquals("Initial", "Photo", "Tags", fillTags(), photo1.getTags())

    photo1.resetTags()
    ok = assertEquals("New", "Photo", "Tags", [], photo1.getTags())

    swText(f"{'Test Passed' if ok else 'Test Failed. Quitting...'}")

    return ok

def testAddTags():
    swText("Add Tags")
    location = "/files/tests/hello.jpg"
    tags = fillTags()
    
    photo1 = photo.Photo(location, fillTags())
    ok = assertEquals("Initial", "Photo", "Tags", tags, photo1.getTags())

    tags += ["Quiet", "Moody"]
    photo1.addTags(["Quiet", "Moody"])
    ok = assertEquals("New", "Photo", "Tags", tags, photo1.getTags())

    swText(f"{'Test Passed' if ok else 'Test Failed. Quitting...'}")
    
    return ok
    
def runTests():
    swText("Testing Photo.py")

    if not testPhoto():
       sys.exit()

    if not testLocation():
        sys.exit()

    if not testResetTags():
        sys.exit()

    if not testAddTags():
        sys.exit()

    swText("Done testing Photo.py")

if __name__ == "__main__":
    runTests()