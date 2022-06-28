#Abstract base classes
#interface
import sys
from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter,QtGui,QPen


class Visualizer:
    
    def __init__(self,lineThickness,peakVolume):
        self.lineThickness = lineThickness
        self.peakVolume = peakVolume

    def draw(self):
        pass
    

#general name for visualizers until decided
class Visualizer1(Visualizer):

    def __init__():
        super().__init__(Visualizer)
    
    def draw(self):
        app = QtGui.QApplication()
        window = QMainWindow()
        #window.setAttribute(Qt.WA_TranslucentBackground, True)
        window.setGeometry(100,0,1000,1000)
        self.window.show()
        
    
        
    
#general name for visualizers until decided
class Visualizer2(Visualizer):
    
    def draw(self):
        pass