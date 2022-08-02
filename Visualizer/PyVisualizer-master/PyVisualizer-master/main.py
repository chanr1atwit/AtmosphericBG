#!/usr/bin/python

import sys
import sounddevice as sd
from scipy.io import wavfile
import numpy as np
#from PySide import QtCore, QtGui

from visualizer import *

app = QtGui.QApplication(sys.argv)

# def record_qt_multimedia():
#     info = QtMultimedia.QAudioDeviceInfo.defaultInputDevice()
#     format = info.preferredFormat()
#     format.setChannels(CHANNEL_COUNT)
#     format.setChannelCount(CHANNEL_COUNT)
#     format.setSampleSize(SAMPLE_SIZE)
#     format.setSampleRate(SAMPLE_RATE)

#     if not info.isFormatSupported(format):
#         print ('Format not supported, using nearest available')
#         format = nearestFormat(format)
#         if format.sampleSize != SAMPLE_SIZE:
#             #this is important, since effects assume this sample size.
#             raise RuntimeError('16-bit sample size not supported!')

#     audio_input = QtMultimedia.QAudioInput(format, app)
#     audio_input.setBufferSize(BUFFER_SIZE)
#     source = audio_input.start()

#     def read_data():
#         data = np.fromstring(source.readAll(), 'int16').astype(float)
#         if len(data):
#             return data
#     return read_data

# def record_pyaudio():
#     p = pyaudio.PyAudio()

#     stream = p.open(format = pyaudio.paInt16,
#                     channels = CHANNEL_COUNT,
#                     rate = SAMPLE_RATE,
#                     input = True,
#                     frames_per_buffer = BUFFER_SIZE)

#     def read_data():
#         data = np.fromstring(stream.read(stream.get_read_available()), 'int16').astype(float)
#         if len(data):
#             return data
#     return read_data

def RecordSoundDevice(self):
     fs = 48000 # Hz
     length = 10 # s
     #recording returns an numpy array
     recording = sd.rec(frames = (int)(fs * length), samplerate=fs,channels=2)
     sd.wait()
     return recording

# try:
#     from PySide import QtMultimedia
#     read_data = record_qt_multimedia()
# except ImportError:
#     print ('Using PyAudio')
#     import pyaudio
#     read_data = record_pyaudio()
read_data = RecordSoundDevice()
def visualizerType(type):
    switch ={
        1: lambda: Line(),
        2: lambda: Spectogram() 
    }

def Line():
    window = LineVisualizer(read_data)
    window.show()
    app.exec_()

def Spectogram():
    window = Spectogram(read_data)
    window.show()
    app.exec_()
