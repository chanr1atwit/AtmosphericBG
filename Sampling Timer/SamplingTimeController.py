#SamplingTimeController class, last edited 6/12/2022
class SamplingTimeController:

    def __init__(self,sampleTime,waitTime){
        self.sampleTime = sampleTime
        self.waitTime = waitTime
    }

    def getSampleTime(self){
        return self.sampleTime
    }

    def getWaitTime(self){
        return self.waitTime
    }

    def setSampleTime(self,sampleTime){
        return self.sampleTime = sampleTime
    }

    def setWaitTime(self,waitTime){
        return self.waitTime = waitTime
    }
