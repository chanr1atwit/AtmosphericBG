#move control functions to controller
class VisualizerModel:
   
    def __init__(self,visualizerList,chosenVisualizer):
        self.visualizerList = visualizerList
        self.chosenVisualizer = chosenVisualizer
    
    def setChosenVisualizer(self,type):
        self.chosenVisualizer = type

    def activateVisualizer(self,chosenVisualizer):
       pass
    
    def deactivate(self):
       pass