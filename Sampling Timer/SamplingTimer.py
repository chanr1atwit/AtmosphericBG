#SamplingTimer class, last edited 7/25/2022
import time
import threading
import essentia
import essentia.standard as ess
import essentia.streaming


'''
TASKS:


'''
class SamplingTimer:

    def __init__(self,sampleTime,waitTime,audio):
        self.sampleTime = sampleTime
        self.waitTime = waitTime
        self.mainThread = threading.Thread(target=self.mainSample)
        self.audio = ess.MonoLoader(filename=audio)
        self.model = TensorflowPredictEffnetDiscogs(graphFilename="discogs-effnet-bs64-1.pb")
        self.activations = model(self.audio)

    #We need a lock
    def mainSample(self):
        self.exit_flag = False
        while not self.exit_flag:
            self.finished = False
            threading.Thread(target=self.timer, args=(self.getSampleTime(),))
            while not self.finished:
                #Does actual sample
                self.performAnalysis()
            self.finished = False
            threading.Thread(target=self.timer, args=(self.getWaitTime(),))
            while not self.finished:
                continue

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
        time.sleep(self.sampleTime)

    def sampleBPM(self):
        #returns the bgm based data from essential
        self.rhythm_extractor = ess.RhythmExtractor2013(method="multifeature")
        bpm, beats, beats_confidence, _, beats_intervals = rhythm_extractor(self.audio)
        return bpm, beats, beats_confidence, _, beats_intervals
