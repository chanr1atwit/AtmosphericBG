# WSL main application, runs in the background and performs essentia analysis
# Interacts with the main application through IPC sockets

#import essentia.standard as ess
from os import remove
from time import sleep
from Socket.Socket import *

#model = ess.TensorflowPredictMusiCNN(graphFilename="Files/genre_tzanetakis-musicnn-msd-1.pb")
sampleRate = 48000

# It converts the array of wav files to a single wav file and the model analyzes the audioResult.wav.
def performAnalysis(audioFile):
    #Uses the model
    #string = audioFile.replace('\\', '/')
    #audio = ess.MonoLoader(filename=string, sampleRate=self.sampleRate)
    #activations = model(audio)
    print(audioFile)

    #remove(string)

    return [0.7] # activations

def recv(connection):
    return connection.recv(1024).decode()

def send(connection, msg):
    connection.send(msg.encode())

if __name__ == "__main__":
    socket = Socket(6000, "bind", host='127.0.0.1')
    socket.listen(1)
    connection, address = socket.accept()
    print("found connection")
    while True:
        msg = recv(connection)

        # Functions on message, causes another recv in some cases
        if msg == 'read':
            print("read received")
            second = recv(connection)
            activations = performAnalysis(second)
            send(connection, str(activations))

        elif msg == 'set':
            print("set received")
            second = recv(connection)
            sampleRate = int(second)

        # Realistically this won't be used, but just in case
        # we decide to implement
        elif msg == 'get':
            print("get received")
            send(connection, str(sampleRate))

        elif msg == 'close':
            print("close received")
            connection.close()
            break
        print("end of iteration")
    socket.close()