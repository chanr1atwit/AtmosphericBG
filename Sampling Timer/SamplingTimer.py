#SamplingTimer class, last edited 7/25/2022
import time
import threading
import essentia
import essentia.standard as ess
import essentia.streaming
import numpy as np
from os import getcwd
from scipy.io.wavfile import write

'''
TASKS:


'''
class SamplingTimer:

    #the audio parameter is a string path to the audio file.
    def __init__(self,sampleTime,waitTime):
        self.samRate = 48000
        self.sampleTime = sampleTime
        self.waitTime = waitTime
        self.mainThread = threading.Thread(target=self.mainSample)
        self.model = TensorflowPredictMusiCNN(graphFilename="genre_tzanetakis-musicnn-msd-1.pb")
        self.count = 0
        self.offset = 0
        self.array = np.zeros(48000*15)

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

    def appendAudio(self, audioPath):
        if self.offset == 14:
            self.offset = 0
        loader = ess.MonoLoader(filename=f"{audioPath}\\{self.offset}",sampleRate=self.samRate)
        audio = loader()
        self.array[self.offset*self.samRate:(self.offset+1)*self.samRate] = audio
        #np.append(self.array,audio)
        self.offset+=1

    def timer(self,timer):
        time.sleep(timer)
        self.finished = True

    def getSampleTime(self):
        return self.sampleTime

    def getWaitTime(self):
        return self.waitTime

    def setSampleTime(self,sampleTime):
        self.sampleTime = sampleTime

    def setWaitTime(self,waitTime):
        self.waitTime = waitTime

    def performAnalysis(self):
        #Uses the model
        scaled = np.int16(self.array/np.max(np.abs(self.array)) * 32767)
        write(f"{getcwd()}\\TemporaryFiles\\audioResult.wav",self.samRate, scaled)
        audio = ess.MonoLoader(filename=f"{getcwd()}\\TemporaryFiles\\audioResult.wav",sampleRate=self.samRate)
        self.activations = self.model(audio)
        #time.sleep(self.sampleTime)

    def sampleBPM(self):
        #returns the bgm based data from essential
        self.rhythm_extractor = ess.RhythmExtractor2013(method="multifeature")
        bpm, beats, beats_confidence, _, beats_intervals = rhythm_extractor(self.array)
        return bpm, beats, beats_confidence, _, beats_intervals
