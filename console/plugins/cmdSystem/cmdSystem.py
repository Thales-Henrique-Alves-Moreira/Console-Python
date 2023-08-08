from prettytable import PrettyTable
import json

import os
import sys
import shutil
from .utils import utils

curDirectory = "C:/"

def cmd(commandLine):
    if len(commandLine.split(' ', 1)) > 1:
        command = commandLine.split(' ', 1)[1]
    else:
        print("Please write the prompt!")
        return

    os.system(command)

def clear(commandLine):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def leave(commandLine):
    exit()

def echo(commandLine):
    msg = commandLine.split(" ", 1)
    del msg[0]

    msg = msg[0]

    print(msg)

def dir(commandLine):
    try:
        files = os.listdir(curDirectory)
    except PermissionError:
        print("You dont have access to these files")
        return

    
    table = PrettyTable(["File", "Size"])

    for i in range(len(files)):
        name = str(files[i])

        try:
            size = os.path.getsize(curDirectory + name)
        except:
            size = 0000

        size = '%.4s' % str(((size/1024)/1024)/1024)
        size += "GB"

        table.add_row([name, size])

    print(table)

def maked(commandLine):
    folder = commandLine.split(" ", 1)
    del folder[0]

    folder = folder[0]

    path = os.path.join(curDirectory, folder)
    os.mkdir(path)

def currentd(commandLine):
    print(curDirectory)

def copyd(commandLine):
    folder = commandLine.split('"')
    del folder[0]
    del folder[1]

    lowerDiskVolume = lambda s: s[:1].lower() + s[1:] if s else ''

    folder1 = lowerDiskVolume(folder[0])
    folder2 = lowerDiskVolume(folder[1])

    # ainda precisa de mudar o utils.check(folder2) e o de baixo

    repeatedName = False

    if utils.checkContainDiskVolume(folder1):
        fileName = os.path.basename(folder1)

        if os.path.exists("copies/" + fileName):
            shutil.rmtree("copies/" + fileName)
    
        shutil.copytree(folder1, "copies/" + fileName)        
        shutil.move('copies/' + fileName, curDirectory + folder2)     
        
    elif utils.checkContainDiskVolume(folder2):
        fileName = os.path.basename(folder1)

        if os.path.exists("copies/" + fileName):
            shutil.rmtree("copies/" + fileName)
    
        shutil.copytree(folder1, "copies/" + fileName)

        while(True):
            if os.path.exists(curDirectory + folder2 + f"/{fileName}"):
                os.rename("copies/" + fileName, "copies/" + fileName + " (COPY)")
                fileName += " (COPY)"
            else:
                break

        shutil.move('copies/' + fileName, curDirectory + folder2)

    elif utils.checkContainDiskVolume(folder1):
        shutil.copytree(folder1, curDirectory + folder2)
    
    elif utils.checkContainDiskVolume(folder1) and utils.checkContainDiskVolume(folder2):
        shutil.copytree(folder1, folder2)
    
    else:
        fileName = os.path.basename(curDirectory + folder1)

        if os.path.exists("copies/" + fileName):
            shutil.rmtree("copies/" + fileName)
    
        shutil.copytree(curDirectory + fileName, "copies/" + fileName)

        while(True):
            if os.path.exists(curDirectory + folder2 + f"/{fileName}"):
                os.rename("copies/" + fileName, "copies/" + fileName + " (COPY)")
                fileName += " (COPY)"
            else:
                break

        shutil.move('copies/' + fileName, curDirectory + folder2)
        

def deld(commandLine):
    folder = commandLine.split(" ", 1)
    del folder[0]

    folder = folder[0]

    if "C:/" in folder:
        shutil.rmtree(folder)
    else:
        shutil.rmtree(curDirectory + folder)

def rend(commandLine):
    folder = commandLine.split('"')
    del folder[0]
    del folder[1]

    name = folder[0]
    newName = folder[1]

    os.rename(name, newName)

def readf(commandLine):
    folder = commandLine.split(" ", 1)
    del folder[0]

    folder = folder[0]

    if "C:/" not in folder or "c:/" not in folder:
        folder = curDirectory + folder

    with open(folder, "r") as file:
        for line in file.readlines():
            print(line)

def editf(commandLine):
    folder = commandLine.split(" ", 1)
    del folder[0]

def changed(commandLine):
    global curDirectory

    if commandLine == "cd":
        currentd(commandLine)
        return

    if '"' not in commandLine:
        folder = commandLine.split(" ", 1)[1]
    elif commandLine.split(" ", 1)[1] != "..":
        folder = commandLine.split('"')[1].replace('\\', '/')        
    else:
        folder = ".."

    if folder == "..":
        if curDirectory == "C:/":
            print("You cant return futhermore")
            return

        curDirectory = utils.returnDir(curDirectory)
        print(curDirectory)
    elif "C:/" in folder:
        if os.path.exists(folder):
            if not folder.endswith("/"):
                folder += "/"

            curDirectory = folder
            print(curDirectory)
        else:
            print("Directory doesnt exists")
    else:
        if utils.checkFile(folder , curDirectory):
            curDirectory += folder + "/"
        
            print(curDirectory)

def printModules(commandLine):
    arg = ""

    if len(commandLine.split()) > 1:
        arg = commandLine.split()[1]

    if arg == "json":
        pathToPlugins = os.path.dirname(sys.argv[0]) + "/plugins"
        modules = os.listdir(pathToPlugins)

        modules.remove("__init__.py")
        modules.remove("__pycache__")

        modulesInfo = []

        for module in modules:
            with open(pathToPlugins + f'/{module}/info.json') as fjson:
                modulesInfo.append(json.load(fjson))

        for i in range(len(modulesInfo)):
            print(modulesInfo[i])

        return

    pathToPlugins = os.path.dirname(sys.argv[0]) + "/plugins"
    modules = os.listdir(pathToPlugins)

    modules.remove("__init__.py")
    modules.remove("__pycache__")

    modulesInfo = []

    for module in modules:
        with open(pathToPlugins + f'/{module}/info.json') as fjson:
            modulesInfo.append(json.load(fjson))

    table = PrettyTable(["Name", "Version", "Author"])

    for i in range(len(modulesInfo)):
        table.add_row([modulesInfo[i]["name"], modulesInfo[i]["version"], modulesInfo[i]["author"]])

    print(table)