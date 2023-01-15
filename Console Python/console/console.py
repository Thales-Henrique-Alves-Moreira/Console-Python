from threading import Thread
import json

import cmdSystem
import games
import location
import request

class Console():
    def __init__(self):
        pass

    def readFunctions(self):
        with open("console/functions.json", 'r') as ffjson:
            self.funcsjson = json.load(ffjson)

    def startCmd(self):
        self.readFunctions()
        while True:
            self.execCmd(self.cmdLine())

    def cmdLine(self):
        commandLine = input(">>> ")

        return commandLine

    def checkCommand(self, commandLine):
        comando = commandLine.split()[0]

        for i in range(len(self.funcsjson)):
            for k in range(len(self.funcsjson[i]['spelling'])):
                if type(self.funcsjson[i]['spelling'][k]) == list:
                    for j in range(len(self.funcsjson[i]['spelling'][k])):
                        if self.funcsjson[i]['spelling'][k][j] == comando:
                            func = self.funcsjson[i]['functions'][k]
                            name = self.funcsjson[i]['name']
                            return (name, func)
                else:
                    if self.funcsjson[i]['spelling'][k] == comando:
                        func = self.funcsjson[i]['functions'][k]
                        name = self.funcsjson[i]['name']
                        return (name, func)

        print("Please insert a valid command.")
        return False

    def execCmd(self, commandLine):
        res = self.checkCommand(commandLine)
        if(res == False):
            return

        name, func = res

        func = getattr(globals()[name], func)
        func(commandLine)

C = Console()
C.startCmd()