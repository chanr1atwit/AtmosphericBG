#SamplingTimeController class, last edited 6/12/2022
import time
import threading
import essentia
import essentia.standard as ess
import essentia.streaming

class SamplingTimer:

    def __init__(self,sampleTime,waitTime):
        self.sampleTime = sampleTime
        self.waitTime = waitTime
        self.t1 = threading.Thread(target=self.mainSample)
        self.loader = ess.MonoLoader

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


    def sampleBPM(self,audio):
        #returns the bgm based data from essential
        pass
