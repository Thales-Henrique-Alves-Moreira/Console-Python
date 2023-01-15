#$c
#$ clear = $L['cls', 'clear']
#$;

import os
import shutil
import utils

curDirectory = "C:/"

ev = os.environ

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

    print("+=====================================================================================================+")
    for i in range(len(files)):
        name = str(files[i])

        try:
            size = os.path.getsize(curDirectory + name)
        except:
            size = 0000

        size = '%.4s' % str(((size/1024)/1024)/1024)
        size += "GB"

        print(utils.buildString(name, size))
        print("-"*103)
    
    print("+=====================================================================================================+")

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

    folder1 = folder[0]
    folder2 = folder[1]

    if "C:/" in folder1 or "c:/" in folder1:
        numCopia = utils.getHowManyCopies() + 1
        shutil.copytree(folder1, 'copies/copia' + numCopia)
        shutil.move('copies/copia' + numCopia, curDirectory + folder2)
        
    elif "C:/" in folder2 or "c:/" in folder2:
        shutil.copytree(curDirectory + folder1, folder2)
    elif "C:/" in folder1 and "C:/" in folder2 or "c:/" in folder1 and "c:/":
        shutil.copytree(folder1, folder2)
    else:
        shutil.copytree(curDirectory + folder1, curDirectory + folder2)

def deld(commandLine):
    folder = commandLine.split(" ", 1)
    del folder[0]

    folder = folder[0]

    if "C:/" in folder:
        shutil.rmtree(folder)
    else:
        shutil.rmtree(curDirectory + folder)

def rend(commandLine):
    #rend, [pasta1], [' '], [pasta2]

    folder = commandLine.split('"')
    del folder[0]
    del folder[1]

    name = folder[0]
    newName = folder[1]

    os.rename(name, newName)

def editf(commandLine):
    folder = commandLine.split(" ", 1)
    del folder[0]

def changed(commandLine):
    global curDirectory

    if commandLine == "cd":
        currentd(commandLine)
        return

    folder = commandLine.split(" ", 1)
    del folder[0]

    folder = folder[0]

    if folder == "..":
        if curDirectory == "C:/":
            print("You cant return futhermore")
            return

        curDirectory = utils.returnDir(curDirectory)
        print(curDirectory)
    else:
        if utils.checkFile(folder , curDirectory):
            curDirectory += folder + "/"
        
            print(curDirectory)