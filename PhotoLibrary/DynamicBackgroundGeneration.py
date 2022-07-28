# Provides overhead for the randimage library by setting 
import ctypes
import numpy as np
from matplotlib.colors import ListedColormap
import randimage
import random

NUM_SAMPLES = 256
MOODS = {
    'acoustic'   : [196/256, 150/256, 105/256],
    'aggressive' : [      1,       0,       0],
    'electronic' : [ 67/256,       1,       0],
    'happy'      : [      1, 140/256,  62/256],
    'party'      : [      1,  17/256, 241/256],
    'relaxed'    : [ 58/256,  65/256,       1],
    'sad'        : [ 59/256,  63/256, 182/256]
}
# tags: str[]
# Generates a color map from matplotlib
# based on provided tags. Uses white as
# start and end. 
# Colors: 
#   Acoustic:   light brown
#   Aggressive: red
#   Electronic: yellow/green
#   Happy:      orange
#   Party:      pink
#   Relaxed:    light blue
#   Sad:        deep blue/purple
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

        print(f"last {lastR}, {lastG}, {lastB}")

        # Get rbg values from mood dict
        mood = MOODS[tags[i]]
        r = mood[0]
        g = mood[1]
        b = mood[2]

        print(f"curr {r*256}, {g*256}, {b*256}")


        # Change respective range from last to current
        vals[begin : end, 0] = np.linspace(lastR, r, NUM_SAMPLES) #R
        vals[begin : end, 1] = np.linspace(lastB, g, NUM_SAMPLES) #G
        vals[begin : end, 2] = np.linspace(lastG, b, NUM_SAMPLES) #B

        lastR = r
        lastG = g
        lastB = b

    
    print(f"last {lastR*256}, {lastG*256}, {lastB*256}")

    # Last -> White
    begin = len(tags) * NUM_SAMPLES
    end = (len(tags) + 1) * NUM_SAMPLES
    vals[begin : end, 0] = np.linspace(lastR, 1, NUM_SAMPLES) #R
    vals[begin : end, 1] = np.linspace(lastB, 1, NUM_SAMPLES) #G
    vals[begin : end, 2] = np.linspace(lastG, 1, NUM_SAMPLES) #B

    return ListedColormap(vals), N

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
    # Get dimensions
    dims = getDimensions(dimensions)
    
    # Generate color maps using randimage
    colormap, length = generateColormap(tags)

    # Generate image using randimage
    randimage.get_random_image(dimensions, colormap)

    # Save image using matplotlib
    

    # Return image location as string
    return link
    

# FOR TESTING
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
def plot_examples(cms):
    """
    helper function to plot two colormaps
    """
    np.random.seed(19680801)
    data = np.random.randn(30, 30)

    fig, axs = plt.subplots(1, 2, figsize=(12, 6), constrained_layout=True)
    for [ax, cmap] in zip(axs, cms):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-8, vmax=8)
        fig.colorbar(psm, ax=ax)
    plt.show()

colormap, length = generateColormap(['party'])
viridis = cm.get_cmap('viridis', 256)

plot_examples([viridis,colormap])