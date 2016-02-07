class Picture:
    def __init__(self, grid):
        self.grid = grid

    def getWidth(self):
        return len(self.grid[0])

    def getHeight(self):
        return len(self.grid)

    def getCell(self, r, c):
        return self.grid[r][c]

    def setCell(self, r, c, value):
        self.grid[r][c] = value

    def compare(self, otherPic):
        return all([otherPic.grid[r][c] == self.grid[r][c] 
                        for c in range(self.getWidth())
                        for r in range(self.getHeight())])
