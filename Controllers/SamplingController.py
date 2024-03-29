import json
import numpy as np
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
        self.metadata = json.load(open('Files\\genre_tzanetakis-musicnn-msd-1.json', 'r'))

        self.socket = Socket(6000, "connect", host='127.0.0.1')

    # Tell essentia main to anaylze the provided file
    def requestPerformAnalysis(self):
        self.socket.send('read')
        self.socket.recv()
        self.socket.send('song.wav')
        self.socket.recv()
        data = self.socket.recv()
        
        activations = data
        while True:
            activations += data
            if data[len(data)-2:len(data)] == "]]":
                break
            data = self.socket.recv()

        
        # Remove OK
        print(activations)
        activations = activations[0:len(activations)-2]

        activations = activations.replace(']', ' ')
        activations = activations.replace('[', ' ')

        count = 0
        activationsLists = []
        current = []
        for item in activations.split(' '):
            if item == '' or item == '\n' or item == '\r':
                continue
            count += 1
            
            current += [item]
            if count % 10 == 0:
                activationsLists += [current]
                current = []

        activationFloats = np.array(activationsLists).astype(np.float32)

        tags = self.parseTags(activationFloats)
        self.core.sendTags(tags)

    # Alert essentia main that app is shutting down
    def requestClose(self):
        self.socket.send('close')
        self.socket.recv()
        self.socket.recv()
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
        self.socket.recv()
        self.socket.send(str(waitTime))
        self.waitTime = waitTime

    #Returns the waitTime
    def getWaitTime(self):
        return self.waitTime

    # Parse tags provided by essentia
    def parseTags(self, activations):
        tags = []
        #count = 0
        meanActivations = activations.mean(axis=0)
        m = np.argmax(meanActivations, axis=0)
        tags += [self.CONVERSIONS[self.metadata['classes'][m]]]

        #for label, probability in zip(self.metadata['classes'], activations.mean(axis=0)):
            #if int(float(probability) * 100) > 50:
                # Convert from metadata tag into actual tag
                #tags.append(self.CONVERSIONS[label])
            #count+=1
        return tags
