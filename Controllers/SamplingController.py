import json
from os import getcwd
from Socket.Socket import *

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

    def __init__(self, core, sampleTime=15, sampleRate=48000):
        self.core = core
        self.sampleRate = sampleRate
        self.sampleTime = sampleTime

        # Set the wait time from configurations (if applicable),
        # use default otherwise.
        waitTime = self.core.getConfiguration("Sampling", "wait", str)
        if waitTime != "":
            self.waitTime = int(waitTime)
        else:
            self.waitTime = 45
        self.metadata = json.load(open('Files\\genre_tzanetakis-musicnn-msd-1.json', 'r'))['classes']

        self.socket = Socket(6000, "connect", host='127.0.0.1')

    # Tell essentia main to anaylze the provided file
    def requestPerformAnalysis(self):
        self.socket.send('read')
        self.socket.send(f'{getcwd()}/TemporaryFiles/song.wav')
        activationsString = self.socket.recv()
        activationsFloats = activationsString.strip('[]').split(', ')
        activations = [float(i) for i in activationsFloats]
        
        tags = self.parseTags(activations)
        self.core.sendTags(tags)

    # Alert essentia main that app is shutting down
    def requestClose(self):
        self.socket.send('close')
        self.socket.close()

    #Returns the sampleTime
    def getSampleTime(self):
        return self.sampleTime

    #Considerations of scrapping this function because the sampleTime will always be 15.
    def setSampleTime(self,sampleTime):
        self.sampleTime = sampleTime

    #waitTime can be configured in the
    def setWaitTime(self,waitTime):
        self.socket.send('set')
        self.socket.send(str(waitTime))
        self.waitTime = waitTime

    #Returns the waitTime
    def getWaitTime(self):
        return self.waitTime

    # Parse tags provided by essentia
    def parseTags(self, activations):
        tags = []
        count = 0
        for label, probability in zip(self.metadata, activations):
            if int(float(probability) * 100) > 50:
                # Convert from metadata tag into actual tag
                tags.append(self.CONVERSIONS[label])
            count+=1
        return tags
