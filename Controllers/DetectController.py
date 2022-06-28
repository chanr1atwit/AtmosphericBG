#imports wmi for python, author: Tim Golden
from wmi import*
class DetectController:
    #executable list
    execList = {'Spotify.exe','Discord.exe','msedge.exe','chrome.exe'}
    #constructor with one param
    def __init__(self):
       pass

    def InList(self,name,list):
        for string in list:
            if (name == string):
                return True
        return False
    
    #reads in process names from taskmanager and adds to set
    def DetectSources(self):
        f = wmi.WMI()
        #use a set to remove duplicate 
        arr = set()
        for process in f.Win32_Process():
            # do not read in all processes, just the musical ones
            if(self.InList(process.Name,self.execList)):
                arr.add(process.Name)
        return arr
    #displays list and allows user to select app
    def DisplaySources(self,set):
       for string in set:
            print(str(string))
            print("\n")
    


    
        

