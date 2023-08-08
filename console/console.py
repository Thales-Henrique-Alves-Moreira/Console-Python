import json
import os

from config import *
from plugins import *

class Console():
    def __init__(self):
        pass

    def readFunctions(self):
        self.funcsjson = []
        
        curPath = os.path.dirname(os.path.realpath(__file__))
        paths = os.listdir(curPath + "/plugins")

        paths.remove("__pycache__")
        paths.remove("__init__.py")
        
        for path in paths:
            with open("plugins/" + path + "/functions.json", "r") as ffjson:
                if not os.path.exists(curPath + "/plugins/" + path + "/not-finished.txt"):
                    self.funcsjson.append(json.load(ffjson))

        with open("config/functions.json", "r") as ffjson:
            self.funcsjson.append(json.load(ffjson))

    def startCmd(self):
        self.readFunctions()
        while True:
            self.execCmd(self.cmdLine())

    def cmdLine(self):
        commandLine = input(">>> ")

        return commandLine

    def checkCommand(self, commandLine):
        if not commandLine:
            return None
        elif commandLine.isspace():
            return None
        
        command = commandLine.split()[0]

        for i in range(len(self.funcsjson)):
            for k in range(len(self.funcsjson[i]['spelling'])):
                if type(self.funcsjson[i]['spelling'][k]) == list:
                    for j in range(len(self.funcsjson[i]['spelling'][k])):
                        if self.funcsjson[i]['spelling'][k][j] == command:
                            func = self.funcsjson[i]['functions'][k]
                            name = self.funcsjson[i]['name']
                            return (name, func)
                else:
                    if self.funcsjson[i]['spelling'][k] == command:
                        func = self.funcsjson[i]['functions'][k]
                        name = self.funcsjson[i]['name']
                        return (name, func)

        print(f"'{command}' isn't a valid command.")
        return None

    def execCmd(self, commandLine):
        res = self.checkCommand(commandLine)
        if(res == None):
            return

        name, func = res

        func = getattr(globals()[name], func)
        func(commandLine)

C = Console()
C.startCmd()