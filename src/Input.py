from Picture import Picture

def parseInput(s):
    lines = s.split('\n')
    [nRows, nColumns] = [int(i) for i in lines[0].split()]

    grid = []
    for i in range(nRows):
        grid.append([True if j == '#' else False for j in lines[i+1]
                                                 if j == '#' or j == '.'])

    return Picture(grid)

def readInputFile(filename):
    f = open(filename)
    return parseInput(f.read())
