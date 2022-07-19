#SamplingTimeController class, last edited 6/12/2022
import time
import threading
import essentia
import essentia.standard
import essentia.streaming

class SamplingTimeController:

t1 = threading.Thread(target=waitTime)


    def __init__(self,sampleTime,waitTime):
        self.sampleTime = sampleTime
        self.waitTime = waitTime

    def getSampleTime(self):
        return self.sampleTime

    def getWaitTime(self):
        return self.waitTime

    def setSampleTime(self,sampleTime):
        self.sampleTime = sampleTime

    def setWaitTime(self,waitTime):
        self.waitTime = waitTime

    def waitTime():
        time.sleep(waitTime)

    def sampleBPM(audio):
        #returns the
    #def sampleTime():

bool exit_flag = false
while !exit_flag:
    waitTime()
