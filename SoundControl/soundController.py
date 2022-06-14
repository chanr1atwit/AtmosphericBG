#imports wmi for python, author: Tim Golden
import wmi
class soundController:
    #constructor with one param
    def __init__(self,sourceID):
       self.sourceID = sourceID
    
    #reads in processID from taskmanager and adds to array
    def detectSources(self):
        f = wmi.WMI()
        #use a set to remove duplicate processes
        arr = set()
        #edit for listed executable list
        for process in f.Win32_Process():#error str object not callable
            # do not read in all processes, just the first ten
            #if(len(arr) == 10):
                #return arr
            arr.add(process.Name)
        return arr
    #displays list and allows user to select app
    def selectSources(self,arr):
       print(str(arr))
    
        

