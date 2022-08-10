#!/usr/bin/env python3
import sounddevice as sd
from scipy.io import wavfile
#import SamplingController
from Views.StartAudioGUI import *

class DetectController:
    def __init__(self,core):
        self.core = core
        self.audioGUI = StartAudioGUI(self)

    def audioToWav(self):
        #wav file location
        temp_dir = "TemporaryFiles\\"
        #read in sound from speaker
        fs = 48000 # Hz
        length = 45 # s
        recording = sd.rec(frames = (int)(fs * length), samplerate=fs,channels=2)
        sd.wait()
        wavfile.write(temp_dir + ('song.wav').format(self.fileID), fs, recording)
    
    def hideAll(self):
        self.appSelectGUI.hide()
