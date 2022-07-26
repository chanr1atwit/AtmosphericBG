#imports wmi for python, author: Tim Golden
import wmi

from Views.SelectAppGUI import *

class DetectController:
    #executable list
    #constructor with one param
    def __init__(self, core):
        # Core allows reads and writes to configurations
        self.core = core

        self.appSelectGUI = SelectAppGUI(self)
        
        self.execList = set(['spotify.exe','discord.exe','msedge.exe','chrome.exe'])
        self.selectedSource = None
    
    #reads in process names from taskmanager and adds to set
    def detectSources(self):
        print("begining detection")
        f = wmi.WMI()
        #use a set to remove duplicate 
        arr = set()
        for process in f.Win32_Process():
            # do not read in all processes, just the musical ones
            if process.Name.lower() in self.execList:
                print(f"adding process to list {process.Name}")
                arr.add(process)
        return arr

    def selectSource(self, source):
        self.selectedSource = source
    
    #displays list and allows user to select app
    # NOTE: For testing use only
    def displaySources(self,set):
       for string in set:
            print(str(string.Name),end="\n\n\n")
    


    
        

