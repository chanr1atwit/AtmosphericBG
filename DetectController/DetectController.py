#imports wmi for python, author: Tim Golden
import wmi
class DetectController:
    #constructor with one param
    def __init__(self,sourceID):
       self.sourceID = sourceID
    
    #reads in processID from taskmanager and adds to array
    def DetectSources(self):
        f = wmi.WMI()
        #use a set to remove duplicate 
        arr = set()
        #edit for listed executable list
        for process in f.Win32_Process():
            # do not read in all processes, just the first ten
            #if(len(arr) == 10):
                #return arr
            arr.add(process.Name)
        return arr
    #displays list and allows user to select app
    def SelectSources(self,list):
       print(str(list))
    
        

