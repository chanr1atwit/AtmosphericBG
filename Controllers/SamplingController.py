# This version of Sampling Controller is part of the main application

import json
from os import getcwd
from multiprocessing.connection import Client, Listener

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
#=======
#        self.mainThread = threading.Thread(target=self.mainSample)
#        self.BPMThread = threading.Thread(target=self.sampleBPM)
#        self.model = ess.TensorflowPredictMusiCNN(graphFilename="Files\\genre_tzanetakis-musicnn-msd-1.pb")
#        self.metadata = json.load(open('Files\\genre_tzanetakis-musicnn-msd-1.json', 'r'))['classes']
#        self.offset = 0
#        self.array = np.zeros(self.samRate*15)
#>>>>>>> main

        #addressSend = ('localhost', 6000)
        #self.sendConn = Client(addressSend, authkey=b'cpwrd')

        #addressRecv = ('localhost', 6001)
        #self.listener = Listener(addressRecv, authkey=b'lpwrd')
        #self.recvConn = self.listener.accept()

    # Tell essentia main to anaylze the provided file
    def requestPerformAnalysis(self):
        self.sendConn.send(['read', f'{getcwd()}/TemporaryFiles/audioResult.wav'])
        activations = self.recvConn.recv()
        tags = self.parseTags(activations)
        self.core.sendTags(tags)

    # Alert essentia main that app is shutting down
    def requestClose(self):
        pass
        #self.sendConn(['close'])
        #self.sendConn.close()
        #self.recvConn.close()
        #self.listener.close()

    #Returns the sampleTime
    def getSampleTime(self):
        return self.sampleTime

    #Considerations of scrapping this function because the sampleTime will always be 15.
    def setSampleTime(self,sampleTime):
        self.sampleTime = sampleTime

    #waitTime can be configured in the
    def setWaitTime(self,waitTime):
        self.sendConn.send(['set', waitTime])
        self.waitTime = waitTime

    #Returns the waitTime
    def getWaitTime(self):
        return self.waitTime

    # Parse tags provided by essentia
    def parseTags(self, activations):
        tags = []
        count = 0
        for label, probability in zip(self.metadata, activations.mean(axis=0)):
            if int(float(probability) * 100) > 50:
                # Convert from metadata tag into actual tag
                tags.append(self.CONVERSIONS[label])
            count+=1
        return tags
