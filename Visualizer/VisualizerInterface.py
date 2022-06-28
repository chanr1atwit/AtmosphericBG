#Abstract base classes
#interface
class VisualizerClass:
    
    def __init__(self,lineThickness,peakVolume):
        self.lineThickness = lineThickness
        self.peakVolume = peakVolume

    def draw(self):
        pass

#general name for visualizers until decided
class Visualizer1(VisualizerClass):
    
    def draw(self):
        pass
    
#general name for visualizers until decided
class Visualizer2(VisualizerClass):
    
    def draw(self):
        pass

#general name for visualizers until decided
class Visualizer3__(VisualizerClass):
    
    def draw(self):
        pass