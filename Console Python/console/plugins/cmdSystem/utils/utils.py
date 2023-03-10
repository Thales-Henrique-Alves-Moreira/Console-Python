from operator import truediv
import os
import sys

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