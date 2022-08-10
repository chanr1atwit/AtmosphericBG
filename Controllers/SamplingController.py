#SamplingController class, last edited 7/29/2022
import time
import threading
import essentia
import essentia.standard as ess
import essentia.streaming
import numpy as np
import json
from os import getcwd
from scipy.io.wavfile import write

'''
Tony's Tasks
1. Add code to CoreController ✅
2. Initalize sampler in CoreController ✅
3. Add input boxes for wait time in settings GUI ✅
4. Add wait time to the config file
5. Modify performAnalysis to parse activations into tags. ✅
6. Output an array of tags using the requestChangeBackground(tags) from CoreController.photoLibraryController ✅
7. Tell Rodney to run BPMThread alongside the mainThread
8. Send output of sampleBPM to visualizer
'''
class SamplingController:

    # Shouldn't ever change
    # KVP since switches aren't a thing
    CONVERSIONS = {
        "blu": "Blues",
        "cla": "Classic",
        "cou": "Country",
        "dis": "Disco",
        "hip": "Hip Hop",
        "jaz": "Jazz",
        "met": "Metal",
        "pop": "Pop",
        "reg": "Reggae",
        "roc": "Rock"
    }

    def __init__(self, core, sampleTime=15, samRate=48000):
        self.core = core
        self.samRate = samRate
        self.sampleTime = sampleTime

        # Set the wait time from configurations (if applicable),
        # use default otherwise.
        waitTime = self.core.getConfiguration("Sampling", "wait", str)
        if waitTime != "":
            self.waitTime = int(waitTime)
        else:
            self.waitTime = 45

        self.mainThread = threading.Thread(target=self.mainSample)
        self.BPMThread = threading.Thread(target=self.sampleBPM)
        self.model = ess.TensorflowPredictMusiCNN(graphFilename="Files\\genre_tzanetakis-musicnn-msd-1.pb")
        self.metadata = json.load(open('Files\\genre_tzanetakis-musicnn-msd-1.json', 'r'))['classes']
        self.offset = 0
        self.array = np.zeros(self.samRate*15)

    #We need a lock
    def mainSample(self):
        self.exit_flag = False
        while not self.exit_flag:
            self.finished = False
            threading.Thread(target=self.timer, args=(self.getSampleTime(),)).start()
            workdone = False
            while not self.finished:
                #Does actual sample
                if self.offset == 14 and not workdone:
                    self.performAnalysis()
            self.finished = False
            threading.Thread(target=self.timer, args=(self.getWaitTime(),)).start()
            while not self.finished:
                continue

    #the audioPath parameter is a string path to the audio file.
    def appendAudio(self, audioPath):
        if self.offset == 14:
            self.offset = 0
        self.loader = ess.MonoLoader(filename=f"{audioPath}\\song{self.offset}.wav",sampleRate=self.samRate)
        audio = self.loader()
        self.array[self.offset*self.samRate:(self.offset+1)*self.samRate] = audio
        self.offset+=1

    #Creates a time buffer for the while loop in mainSample to do work.
    def timer(self,timer):
        time.sleep(timer)
        self.finished = True

    #Returns the sampleTime
    def getSampleTime(self):
        return self.sampleTime

    #Returns the waitTime
    def getWaitTime(self):
        return self.waitTime

    #Considerations of scrapping this function because the sampleTime will always be 15.
    def setSampleTime(self,sampleTime):
        self.sampleTime = sampleTime

    #waitTime can be configured in the
    def setWaitTime(self,waitTime):
        self.waitTime = waitTime

    #It converts the array of wav files to a single wav file and the model analyzes the audioResult.wav.
    def performAnalysis(self):
        #Uses the model
        scaled = np.int16(self.array/np.max(np.abs(self.array)) * 32767)
        write(f"{getcwd()}\\TemporaryFiles\\tempAudio.wav",self.samRate, scaled)
        audio = ess.MonoLoader(filename=f"{getcwd()}\\TemporaryFiles\\audioResult.wav",sampleRate=self.samRate)
        activations = self.model(audio)
        tags = self.parseTags(activations)
        self.core.sendTags(tags)

    #This function returns a set of output data related to BPM.
    def sampleBPM(self):
        #returns the bgm based data from essential
        self.rhythm_extractor = ess.RhythmExtractor2013(method="multifeature")
        bpm, beats, beats_confidence, __, beats_intervals = rhythm_extractor(self.loader)
        return bpm, beats, beats_confidence, beats_intervals

    def parseTags(self, activations):
        tags = []
        count = 0
        for label, probability in zip(self.metadata['classes'], activations.mean(axis=0)):
            if int(float(probability) * 100) > 50:
                # Convert from metadata tag into actual tag
                tags.append(self.CONVERSIONS[label])
            count+=1
        return tags
