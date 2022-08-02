# Provides overhead for the randimage library by setting 
import ctypes
import numpy as np
import matplotlib
from matplotlib.colors import ListedColormap
import randimage.randimage as randimage
import random

NUM_SAMPLES = 256
GENRES = {
    'Blues'   : [59/256,  63/256,  182/256],
    'Classic' : [196/256, 150/256, 105/256],
    'Country' : [1,       140/256, 62/256],
    'Disco'   : [58/256,  65/256,  1],
    'Hip Hop' : [248/256, 242/256, 56/256],
    'Jazz'    : [71/256,  16/256,  224/256],
    'Metal'   : [1,       0,       0],
    'Pop'     : [67/256,  1,       0],
    'Reggae'  : [0,       207/256, 49/256],
    'Rock'    : [1,       17/256,  241/256]
}

# tags: str[]
# Generates a color map from matplotlib
# based on provided tags. Uses white as
# start and end. 
def generateColormap(tags):
    # Number of colors based on present tags
    # +1 zone for white
    N = (len(tags) + 1) * NUM_SAMPLES    

    # Shuffle the tags for a random order
    random.shuffle(tags)

    # Color values in a numpy array
    vals = np.ones((N, 4))

    # Store previous end values for next iteration,
    # begin at white 
    lastR = 1
    lastG = 1
    lastB = 1

    for i in range(len(tags)):
        # Get indicies for range
        begin = i * NUM_SAMPLES 
        end = (i + 1) * NUM_SAMPLES   

        # Get rbg values from mood dict
        genre = GENRES[tags[i]]
        r = genre[0]
        g = genre[1]
        b = genre[2]

        # Eventually want to add check to see if
        # intersection of two colors is gross (gray)
        # looking, then intersect with white instead.
        # This will need to be before for loop.

        # Change respective range from last to current
        vals[begin : end, 0] = np.linspace(lastR, r, NUM_SAMPLES) #R
        vals[begin : end, 1] = np.linspace(lastG, g, NUM_SAMPLES) #G
        vals[begin : end, 2] = np.linspace(lastB, b, NUM_SAMPLES) #B

        lastR = r
        lastG = g
        lastB = b

    # Last -> White
    begin = len(tags) * NUM_SAMPLES
    end = (len(tags) + 1) * NUM_SAMPLES
    vals[begin : end, 0] = np.linspace(lastR, 1, NUM_SAMPLES) #R
    vals[begin : end, 1] = np.linspace(lastG, 1, NUM_SAMPLES) #G
    vals[begin : end, 2] = np.linspace(lastB, 1, NUM_SAMPLES) #B

    return ListedColormap(vals), N

# custom: int[2]
# Return either the custom dimensions of the photo or 
# the current size of the users display (manually downscaled).
# Output reversed to (height, width).
def getDimensions(custom=None):
    if custom is not None and len(custom) == 2:
        return (custom[1], custom[0])
    return (int(ctypes.windll.user32.GetSystemMetrics(1)/4),
            int(ctypes.windll.user32.GetSystemMetrics(0)/4))

# tags: str[]
# Create a background and save it
# Hook for PL
def generateImage(tags, link, dimensions=None):
    # Get dimensions
    dims = getDimensions(dimensions)

    # Get random tag for spice
    tags += [random.choice(list(GENRES.keys()))]

    # Generate color maps using randimage
    colormap, length = generateColormap(tags)

    # Generate image using randimage
    image = randimage.get_random_image(dims, colormap)

    # Save image using matplotlib
    matplotlib.pyplot.imsave(link, image)
