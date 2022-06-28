#Abstract base classes
#interface
class VisualizerSuper:
    
    def __init__(self,lineThickness,peakVolume):
        self.lineThickness = lineThickness
        self.peakVolume = peakVolume

    def draw(self):
        pass
    
    

