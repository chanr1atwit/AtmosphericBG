# Main function to run project
if __name__ == "__main__":
    #from PhotoLibrary import DynamicBackgroundGeneration as DBG
    #import matplotlib
    #import ctypes
    #import time
    #import os
    ###colormap, length = DBG.generateColormap(['party','electronic','happy'])
    ##viridis = DBG.cm.get_cmap('viridis', 768)

    ##print(f"{DBG.generateImage(['party','electronic','happy'])}")
    #start = time.time()
    #DBG.temp()
    
    #link = f"{os.getcwd()}\\photo.png"
    #ctypes.windll.user32.SystemParametersInfoW(20, 0, link, 0)
    #print(f"Time elapsed: {time.time() - start}")

    ##DBG.plot_examples([viridis,colormap])
    from Controllers.CoreController import CoreController
    import sys
    CoreController(sys.argv)
