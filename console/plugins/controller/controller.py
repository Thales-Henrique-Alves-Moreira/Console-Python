from concurrent.futures import thread
from operator import truediv
#import pyserial
from threading import Thread

controllerActive = False

def cStart(commandLine):
    global controllerActive
    controllerActive = True

    t = Thread(target=mainControllerThread)
    t.start()

def cStop(commandLine):
    global controllerActive
    controllerActive = False

def getUrl():
    pass

def mainControllerThread():
    while controllerActive:
        ipt = ""

        if ipt == "pause":
            pass
        elif ipt == "continue":
            pass
        elif ipt == "pass10s":
            pass
        elif ipt == "return10s":
            pass
        elif ipt == "returnPage":
            pass
        elif "search" in ipt:
            url = getUrl()

            if url == "youtube":
                pass
            elif url == "netflix":
                pass
            
        elif "goSite" in ipt:
            ws = ipt.split("%$qrry%")[1]
        elif ipt == "goDown":
            url = getUrl()

            if url == "youtube":
                pass
            elif url == "netflix":
                pass
            
        elif ipt == "goUp":
            url = getUrl()
            
            if url == "youtube":
                pass
            elif url == "netflix":
                pass

        elif ipt == "goLeft":
            url = getUrl()
            
            if url == "youtube":
                pass
            elif url == "netflix":
                pass

        elif ipt == "goRight":
            url = getUrl()
            
            if url == "youtube":
                pass
            elif url == "netflix":
                pass

        else:
            print("Error 1 in controller, unknown command")