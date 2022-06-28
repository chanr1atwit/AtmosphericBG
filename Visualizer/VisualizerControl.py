#NEED TO FIX
#USES MATPLOTLIB AND NUMPY FFT
import VisualizerSuper
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft
from matplotlib.animation import FuncAnimation


class VisualizerBasic(VisualizerSuper):
    fig = plt.figure()
    ax = fig.add_subplot(100,100,0)
    #initialize
    def __init__(self,peakVolume,lineThickness):
        self.peakVolume = peakVolume
        self.lineThickness = lineThickness
    
    
    #turn into array
    def fileToArray():
        #import sounds from essentia(Empty for now)
        musicFile = musicFile = ""
        #read in file
        f = open(musicFile, "r")
        #display every line as fft graph
        for x in f:
            update(x)
    
    #use fft function
    def update(frame,array):
       fft(array)

    
    #animate using graph
    def animate():
        anim = FuncAnimation(fig, update, frames=range(8), interval=1000)

    
