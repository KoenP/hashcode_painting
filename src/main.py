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
        print(str(emptyPicture))
    # check if pictures are the same
    return picture.compare(emptyPicture)


# read input
args = sys.argv
picture = readInputFile(args[1])

# simple solve
simple_actions = simpleSolve(picture)

# eval function
print(evalPicture(simple_actions, picture))
