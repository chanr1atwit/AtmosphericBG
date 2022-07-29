# Provides overhead for the randimage library by setting 
import ctypes
import matplotlib as plot
import randimage as img

# custom: int[2]
# Return either the custom dimensions of the photo or 
# the current size of the users display (if manually downscaled)
def getDimensions(custom=None):
    if custom is not None and len(custom) == 2:
        return custom
    return [ctypes.windll.user32.GetSystemMetrics(0),
            ctypes.windll.user32.GetSystemMetrics(1)]

# tags: str[]
# Create a background and save it
# Hook for PL
def generateImage(tags, dimensions=None):
    dims = getDimensions(dimensions)
    #generate color maps using matplotlib and tags
    #generate image using randimage
    #save image using matplotlib
    #return image location as string
    print(f"{dims[0]}, {dims[1]}")
    