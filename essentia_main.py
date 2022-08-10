# WSL main application, runs in the background and performs essentia analysis
# Interacts with the main application through IPC sockets

import essentia.standard as ess
from os import remove
from multiprocessing.connection import Client, Listener

model = ess.TensorflowPredictMusiCNN(graphFilename="Files/genre_tzanetakis-musicnn-msd-1.pb")
sampleRate = 48000

# It converts the array of wav files to a single wav file and the model analyzes the audioResult.wav.
def performAnalysis(audioFile):
    #Uses the model
    string = audioFile.replace('\\', '/')
    audio = ess.MonoLoader(filename=string, sampleRate=self.sampleRate)
    activations = model(audio)

    remove(string)

    return activations

if __name__ == "__main__":
    addressRecv = ('localhost', 6000)
    listener = Listener(addressRecv, authkey=b'cpwrd')
    recvConn = listener.accept()

    addressSend = ('localhost', 6001)
    sendConn = Client(addressSend, authkey=b'lpwrd')

    while True:
        msg = recvConn.recv()

        # Functions on message, causes another recv in some cases
        if msg[0] == 'read':
            activations = performAnalysis(msg[1])
            sendConn.send(activations)

        elif msg[0] == 'set':
            sampleRate = int(msg[1`])

        # Realistically this won't be used, but just in case
        # we decide to implement
        elif msg[0] == 'get':
            sendConn.send(str(sampleRate))

        elif msg[0] == 'close':
            recvConn.close()
            sendConn.close()
            break
    
    listener.close()
