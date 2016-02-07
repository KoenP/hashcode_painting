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

    @staticmethod
    def makeEmptyPicture(nRows, nColumns):
        return Picture([[False] * nColumns] * nRows)
