# GUI superclass, last edited 6/23/2022
from PyQt5 import QtWidgets as QtW
from PyQt5.QtGui import QPainter as Qp
from PyQt5 import QtCore as QtC

class GUI:
    # This function sets up the view
    # NOTE: Uses a reference to the controller
    #       that created this View
    def __init__(self, controller, x, y, name):
        # Access to controller functions that do the work
        self.controller = controller

        # Window setup
        self.window = QtW.QMainWindow()
        self.window.setFixedSize(x, y)
        self.window.setWindowTitle(name)
        self.window.setWindowModality(QtC.Qt.ApplicationModal)
        
        sizePolicy = QtW.QSizePolicy(QtW.QSizePolicy.Fixed, QtW.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.window.sizePolicy().hasHeightForWidth())
        
        self.window.setSizePolicy(sizePolicy)

    def show(self):
        self.window.show()

    def hide(self):
        self.window.hide()
