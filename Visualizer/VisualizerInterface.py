#Abstract base classes
import abc
#interface
class VisualizerInterface(abc.ABC):
    @abc.abstractclassmethod
    def draw(self):
        pass

#general name for visualizers until decided
class Visualizer1(VisualizerInterface):
    def __init(self,lineThickness,peakVolume):
        pass

    def draw(self):
        pass
#general name for visualizers until decided
class Visualizer2(VisualizerInterface):
    def __init(self,lineThickness,peakVolume):
        pass

    def draw(self):
        pass
#general name for visualizers until decided
class Visualizer3(VisualizerInterface):
    def __init(self,lineThickness,peakVolume):
        pass

    def draw(self):
        pass