from .Input import *
from .Picture import *
from .Action import *
import sys

def simpleSolve(picture):
    actions = []
    for i in range(picture.getWidth()):
        for j in range(picture.getHeight()):
            if picture.getCell(j, i):
                actions.append(DrawSquare(j,i,0))

    return actions

def eval(actions, picture):
    

def __main__():
    # read input
    args = sys.argv
    picture = readInputFile(args[1])

    # simple solve
    simple_actions = simpleSolve(picture)

    # eval function