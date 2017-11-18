
class World(object):

    def __init__(self):
        self.map = []

    def addCell(self, cell):
        for currentCell in self.map:
            if currentCell.x == cell.x and currentCell.y == cell.y:
                return
        self.map.append(cell)

    def numberOfNeighbors(self, cell):
        xRange = [cell.x - 1, cell.x, cell.x + 1]
        yRange = [cell.y - 1, cell.y, cell.y + 1]

        countNeighbors = 0

        for currentCell in self.map:
            if currentCell.x in xRange and currentCell.y in yRange:
                if currentCell != cell:
                    countNeighbors += 1

        return countNeighbors
