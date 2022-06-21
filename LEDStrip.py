import numpy as np
from time import sleep
import os
import wave
import pyaudio
import time

def Color(red, green, blue):
    """Convert the provided red, green, blue color to a 24-bit color value.
    Each color component should be a value 0-255 where 0 is the lowest intensity
    and 255 is the highest intensity.
    """
    return (red << 16) | (green << 8) | blue

class _LED_Data(object):

    def __init__(self, channel, size):
        self.size = size
        self.channel = channel
    
    def setColor(self, n, color):
        """Set LED at position n to the provided 24-bit color value (in RGB order).
        """
        self._led_data[n] = color

    def setColorRGB(self, n, red, green, blue):
        """Set LED at position n to the provided red, green, and blue color.
        Each color component should be a value from 0 to 255 (where 0 is the
        lowest intensity and 255 is the highest intensity).
        """
        self.setColor(n, Color(red, green, blue))

    def setBrightness(self, brightness):
        """Scale each LED in the buffer by the provided brightness.  A brightness
        of 0 is the darkest and 255 is the brightest.
        """
        self.setBrightness(self._channel, brightness)
        """ws is websockets is a library for building WebSocket servers and clients in Python with a focus on correctness, simplicity, 
           robustness, and performance.
        """
