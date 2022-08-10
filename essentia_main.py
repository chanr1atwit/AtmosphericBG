# WSL main application, runs in the background and performs essentia analysis
# Interacts with the main application through IPC sockets

import essentia.standard as ess
from os import remove, getcwd
from time import sleep
import pickle
from Socket.Socket import *

model = ess.TensorflowPredictMusiCNN(graphFilename="Files/genre_tzanetakis-musicnn-msd-1.pb")
sampleRate = 48000

# It converts the array of wav files to a single wav file and the model analyzes the audioResult.wav.
def performAnalysis(audioFile):
    #Uses the model
    print(f"in perform")
    loader = ess.MonoLoader(filename=audioFile, sampleRate=sampleRate)
    audio = loader()
    activations = pickle.dumps(model(audio))


    #remove(string)

    return activations # activations

def recv(connection):
    return connection.recv(4096)

def send(connection, msg):
    connection.send(msg)

socket = Socket(6000, "bind", host='127.0.0.1')
socket.listen(1)
connection, address = socket.accept()
print("found connection")
while True:
    msg = recv(connection)
    send(connection, 'OK')
    # Functions on message, causes another recv in some cases
    if msg == 'read':
        print("read received")
        second = recv(connection)
        send(connection, 'OK')
        string = f"{getcwd()}/TemporaryFiles/song.wav"
        activations = performAnalysis("TemporaryFiles/song.wav")
        connection.send(activations)

    elif msg == 'set':
        print("set received")
        send(connection, 'OK')
        second = recv(connection)
        sampleRate = int(second)

    # Realistically this won't be used, but just in case
    # we decide to implement
    elif msg == 'get':
        print("get received")
        send(connection, 'OK')
        send(connection, str(sampleRate))

    elif msg == 'close':
        print("close received")
        send(connection, 'OK')
        connection.close()
        break
    print("end of iteration")
socket.close()