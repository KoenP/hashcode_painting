from Action import *
class AI:

    def __init__(self):
        pass

    def lineSolve(self, picture):
        actions = []
        for row in range(picture.getRowCount()):
            start = -1
            for column in range(picture.getColumnCount()):
                if start == -1 and picture.getCell(row, column):
                    start = column
                elif start != -1 and not picture.getCell(row, column):
                    actions.append(DrawLine(row, start, row, column - 1 ))
                    start = -1
            if start != -1:
                actions.append(DrawLine(row, start, row, picture.getColumnCount() - 1))

        return actions

    def solve(self, picture):
        actions = self.lineSolve(picture)
        return actions