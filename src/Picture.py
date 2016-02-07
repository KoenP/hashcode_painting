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


def parseInput(s):
    lines = s.split('\n')
    [nRows, nColumns] = [int(i) for i in lines[0].split()]

    grid = []
    for i in range(nRows):
        grid.append([True if j == '#' else False for j in lines[i+1]
                                                 if j == '#' or j == '.'])

    return Picture(grid)
