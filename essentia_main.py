# WSL main application, runs in the background and performs essentia analysis
# Interacts with the main application through IPC sockets
import sys
sys.path.append('/usr/local/lib/python3/dist-packages/')
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
    loader = ess.MonoLoader(filename=audioFile, sampleRate=sampleRate)
    audio = loader()
    activations = model(audio)
    
    remove(audioFile)

    return str(activations) # activations

def recv(connection):
    return connection.recv(1024).decode()

def send(connection, msg):
    connection.send(msg.encode())

socket = Socket(6000, "bind", host='127.0.0.1')
socket.listen(1)
print("Waiting for main application")
connection, address = socket.accept()
print("Main application found")
while True:
    msg = recv(connection)
    send(connection, 'OK')
    # Functions on message, causes another recv in some cases
    if msg == 'read':
        second = recv(connection)
        send(connection, 'OK')
        activations = performAnalysis("TemporaryFiles/song.wav")
        send(connection, activations)

    elif msg == 'set':
        send(connection, 'OK')
        second = recv(connection)
        sampleRate = int(second)

    # Realistically this won't be used, but just in case
    # we decide to implement
    elif msg == 'get':
        send(connection, 'OK')
        send(connection, str(sampleRate))

    elif msg == 'close':
        send(connection, 'OK')
        connection.close()
        break
socket.close()