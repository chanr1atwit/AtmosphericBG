# GUI superclass, last edited 6/23/2022
from PyQt5 import QtWidgets as QtW
from PyQt5.QtGui import QPainter as Qp
from PyQt5 import QtCore as QtC

class GUI(QtW.QMainWindow):
    # This function sets up the view
    # NOTE: Uses a reference to the controller
    #       that created this View
    def __init__(self, controller, x, y, name):
        # Access to controller functions that do the work
        super(GUI, self).__init__()
        self.controller = controller

        # Window setup
        self.setFixedSize(x, y)
        self.setWindowTitle(name)
        self.setWindowModality(QtC.Qt.ApplicationModal)
        
        sizePolicy = QtW.QSizePolicy(QtW.QSizePolicy.Fixed, QtW.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        
        self.setSizePolicy(sizePolicy)
