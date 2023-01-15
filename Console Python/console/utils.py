from operator import truediv
import os
import sys

def findMiddle(text, space):
    textlen = len(text)

    if(textlen % 2 != 0):
        spaceBetween = (space - textlen) / 2
        space1 = int(spaceBetween) + 1
        space2 = int(spaceBetween) - 1
    else:
        spaceBetween = (space - textlen) / 2
        space1 = spaceBetween
        space2 = spaceBetween

    return (int(space1), int(space2))

def buildString(name, size):
    space1n, space2n = findMiddle(name, 90)
    space1s, space2s = findMiddle(size, 10)

    builtStr = "|" + " " * space1n + name + " " * space2n + " " + " " * space1s + size + " " * 3 + "|"

    return builtStr

def returnDir(folder):
    folder = [*folder]
    countSlashes = 0
    pos1 = 0
    pos2 = 0

    for i in range(len(folder) - 1, -1, - 1):
        if folder[i] == "/" and countSlashes < 2:
            
            if countSlashes == 0:
                pos2 = i + 1
            else:
                pos1 = i + 1

            countSlashes += 1

    del folder[pos1:pos2]
    return ''.join(folder)
    
def checkFile(file, curd):
    if not os.path.exists(curd + file):
        print("Directory doesnt exists")
        return False

    if not os.path.isdir(curd + file):
        print("You cant access files")
        return False
    
    return True

def getHowManyCopies():
    dir = os.listdir("copies")

    cFiles = len(dir)
    return cFiles