from Input import *
from Picture import *
from Action import *
import sys

def simpleSolve(picture):
    actions = []
    for c in range(picture.getColumnCount()):
        for r in range(picture.getRowCount()):
            if picture.getCell(r, c):
                actions.append(DrawSquare(r,c,0))

    return actions

def evalPicture(actions, picture):
    emptyPicture = Picture.makeEmptyPicture(picture.getRowCount(), picture.getColumnCount())
    for action in actions:
        action.perform(emptyPicture)

    # check if pictures are the same
    return picture.compare(emptyPicture)

def output(actions):
    outputStr = str(len(actions)) + "\n"
    for action in actions:
        outputStr += action.toString() + "\n"
    return outputStr

def writeToFile(actions, fileName):
    f = open("../output_files/" + fileName + ".out", "w")
    f.write(output(actions))

# read input
args = sys.argv
picture = readInputFile(args[1])
fileName = args[1].split('.')[0]
# simple solve
simple_actions = simpleSolve(picture)

# eval function
print(evalPicture(simple_actions, picture))

# output function
writeToFile(simple_actions,fileName)
