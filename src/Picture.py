class Picture:
    def __init__(self, grid):
        self.grid = grid

    def getColumnCount(self):
        return len(self.grid[0])

    def getRowCount(self):
        return len(self.grid)

    def getCell(self, r, c):
        return self.grid[r][c]

    def setCell(self, r, c, value):
        self.grid[r][c] = value

    def compare(self, otherPic):
        return all([otherPic.grid[r][c] == self.grid[r][c]
                    for c in range(self.getColumnCount())
                    for r in range(self.getRowCount())])

    def __str__(self):
        s = ""
        for r in range(self.getRowCount()):
            for c in range(self.getColumnCount()):
                s += '#' if self.grid[r][c] else '.'
            s += '\n'
        return s

    @staticmethod
    def makeEmptyPicture(nRows, nColumns):
        return Picture([[False for c in range(nColumns)] for r in range(nRows)])
