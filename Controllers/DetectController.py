#!/usr/bin/env python3
import noisereduce as nr
import sounddevice as sd
from scipy.io import wavfile
from Views.SelectAppGUI import *

class DetectController:
    #executable list
    #constructor with one param
    def __init__(self):
         self.appSelectGUI = SelectAppGUI(self)
         self.fileID = 0
        # self.execList = set(['spotify.exe','discord.exe','msedge.exe','chrome.exe'])
        # self.selectedSource = None
    #read in from speaker and turn into WAV
   
    def AudioToWav(self):
         temp_dir = "TemporaryFiles\\"
         #read in sound from speaker
         #print((sd.query_devices()))
         fs = 48000 # Hz
         length = 0.5 # s
         recording = sd.rec(frames = (int)(fs * length), samplerate=fs,channels=2)
         sd.wait()
         wavfile.write(temp_dir + ('song({0}).wav').format(self.fileID), fs, recording)
         self.fileID += 1
   
  
        
     #     rate, data = wavfile.read(temp_dir + "song.wav")
     #     # perform noise reduction
     #     reduced_noise = nr.reduce_noise(y=data, sr=rate)
     #     wavfile.write(temp_dir + "song.wav", rate, reduced_noise)

  

        

         

    
    #reads in process names from taskmanager and adds to set
    # def detectSources(self):

    #     print("beginning detection")
    #     f = wmi.WMI()
    #     #use a set to remove duplicate 
    #     arr = set()
    #     for process in f.Win32_Process():
    #         # do not read in all processes, just the musical ones
    #         if process.Name.lower() in self.execList and process.Name.lower() not in arr:
    #             arr.add(process.Name.lower())
    #             print(f"adding process to list {process.ProcessID}")
    #             detectButton = ProcessButton(process)
    #             self.appSelectGUI.layout.addWidget(detectButton)
    #             detectButton.clicked.connect(lambda:self.selectSource(process.ProcessID))
              
        

    # def selectSource(self, source):
    #     self.selectedSource = source
    #     print("selectedSource",str (source))
    
    # #displays list and allows user to select app
    # # NOTE: For testing use only
    
    

    # def displaySources(self,set):
    #    for string in set:
    #         print(str(string.Name),end="\n\n\n")

   
    

