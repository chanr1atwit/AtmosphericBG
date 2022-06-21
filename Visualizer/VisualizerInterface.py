#Abstract base classes
import abc
#interface
class VisualizerInterface(abc.ABC):
    @abc.abstractclassmethod
    def draw(self):
        pass

#general name for visualizers until decided
class VisualizerOne(VisualizerInterface):
    def __init(self,lineThickness,peakVolume):
        pass

    def draw(self):
        pass
#general name for visualizers until decided
class VisualizerTwo(VisualizerInterface):
    def __init(self,lineThickness,peakVolume):
        pass

    def draw(self):
        pass
#general name for visualizers until decided
class VisualizerThree(VisualizerInterface):
    def __init(self,lineThickness,peakVolume):
        pass

    def draw(self):
        pass