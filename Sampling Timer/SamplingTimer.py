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
        self.t1 = threading.Thread(target=mainSample)

    def mainSample():
        self.exit_flag = False
        while not self.exit_flag:
            self.finished = False
            threading.Thread(target=timer, args=(getSampleTime(),))
            while not self.finished:
                #Does actual sample
                sampleTime()
            self.finished = False
            threading.Thread(target=timer, args=(getWaitTime(),))
            while not self.finished:
                continue

    def timer(timer):
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

    def sampleTime():

        time.sleep(self.sampleTime)

    def sampleBPM(audio):
        #returns the bgm based data from essential
        pass
