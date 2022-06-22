# MainGUI class, last edited 6/20/2022
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

class MainGUI:
    # This function sets up the MainGUI view
    # NOTE: Uses a reference to the controller
    #       that created this View
    def __init__(self, controller):
        # Access to controller functions that do the work
        self.controller = controller

        # Window setup
        self.window =  QMainWindow()
        self.window.setGeometry(0, 0, 500, 500)
        self.window.setWindowTitle("Atmospheric BG")
        
        # Buttons on View
        pLButton = QtWidgets.QPushButton("Photo Library", self.window)
        pLButton.move(250, 250)
        pLButton.clicked.connect(self.photoLibraryView)

    # Show the MainGUI window
    def show(self):
        self.window.show()

    # List of connected views
    def photoLibraryView(self):
        pass
