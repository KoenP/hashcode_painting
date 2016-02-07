class Action:

    def toString(self):
        raise NotImplementedError("Abstract function")

    def perform(self, Picture):
        raise NotImplementedError("Abstract function")


class DrawSquare(Action):

    def __init__(self, row, column, size):
        self.row = row
        self.column = column
        self.size = size

    def toString(self):
        return "PAINT_SQUARE " + str(self.row) + " " + str(self.column) + " " + str(self.size)

    def perform(self, picture):
        start = (self.column - self.size, self.row - self.size)

        # Row
        for i in range(self.size):
            # Column
            for j in range(self.size):
                picture.setCell(start[0] + j, start[1] + i, True)

class DrawLine(Action):

    def __init__(self, r1, c1, r2, c2):
        self.r1 = r1
        self.c1 = c1
        self.r2 = r2
        self.c2 = c2

    def toString(self):
       return "PAINT_LINE " + str(self.r1) + " "+ str(self.c1) + " " + str(self.r2) + " " + str(self.c2)


    def perform(self, picture):

        if(self.r1 == self.r2):
            start = (min(self.c1, self.c2), self.r1)
            for i in range( abs(self.c1 - self.c2) ):
                picture.setCell(start[0] + i, start[1], True)


        elif(self.c1 == self.c2):
            start = (self.c1, min(self.r1, self.r2))
            for i in range( abs(self.r1 - self.r2) ):
                picture.setCell(start[0], start[1] + i, True)

        else:
            raise Exception("coordinates mismatch")

class Erase(Action):

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def toString(self):
        return "ERASE_CELL " + str(self.row) + " " + str(self.column)

    def perform(self, picture):
        picture.setCell(self.row, self.column, False)

