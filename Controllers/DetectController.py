#imports wmi for python, author: Tim Golden
import wmi

from Views.SelectAppGUI import *

class DetectController:
    #executable list
    #constructor with one param
    def __init__(self):
        self.appSelectGUI = SelectAppGUI(self)
        self.execList = set(['spotify.exe','discord.exe','msedge.exe','chrome.exe'])
        self.selectedSource = None
    
    #reads in process names from taskmanager and adds to set
    def detectSources(self):

        print("beginning detection")
        f = wmi.WMI()
        #use a set to remove duplicate 
        arr = set()
        i = 250
        for process in f.Win32_Process():
            # do not read in all processes, just the musical ones
            if process.Name.lower() in self.execList:
                print(f"adding process to list {process.ProcessID}")
                detectButton = ProcessButton(process,self.appSelectGUI)
                detectButton.setGeometry(350,i,131,40)      
                detectButton.clicked.connect(lambda:self.selectSource(process.ProcessID))
                i += 50
        

    def selectSource(self, source):
        self.selectedSource = source
        print("selectedSource",str (source))
    
    #displays list and allows user to select app
    # NOTE: For testing use only
    def AudioToWav(self):
        pass
    

    def displaySources(self,set):
       for string in set:
            print(str(string.Name),end="\n\n\n")
    

