#imports wmi for python, author: Tim Golden
import wmi
class soundController:
    #constructor with one param
    def __init__(self,sourceID):
       self.sourceID = sourceID
    #reads in processID from taskmanager and adds to array
    def detectSources():
        f = wmi.WMI()
        arr = []
        for process in f.win32.Process():
            if(len(arr) == 10):
                return arr
            arr += [process.ProcessID()]
    #displays list and allows user to select app
    def selectSources():
        pass
    

        

