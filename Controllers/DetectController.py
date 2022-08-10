from os import remove
import threading
import sounddevice as sd
from scipy.io import wavfile
from Views.StartAudioGUI import *

class DetectController:
    def __init__(self,core):
        self.core = core
        self.audioGUI = StartAudioGUI(self)
        self.thread = None
        self.kill = True

    def start(self):
        self.kill = False
        self.thread = threading.Thread(target=self.audioToWav)
        self.thread.start()
        self.audioGUI.startRecord.setEnabled(False)
        self.audioGUI.endRecord.setEnabled(True)

    def stop(self):
        if self.thread is None:
            return
        else:
            # Thread will join on its own
            print("Signal sent to stop recording after current process finishes.")
            self.kill = True
            self.audioGUI.startRecord.setEnabled(True)
            self.audioGUI.endRecord.setEnabled(False)

    def audioToWav(self):
        while not self.kill:
            #wav file location
            temp_dir = "TemporaryFiles\\"
            #read in sound from speaker
            fs = 48000 # Hz
            length = 1 # s
            recording = sd.rec(frames = (int)(fs * length), samplerate=fs,channels=2)
            sd.wait()
            try:
                remove(temp_dir + 'song.wav')
            except:
                pass
            wavfile.write(temp_dir + 'song.wav', fs, recording)
            self.core.requestAnalysis()
    
    def hideAll(self):
        self.appSelectGUI.hide()
