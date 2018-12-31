from utils.utils import file_get_contents
import numpy as np

def generateCoordinates(x, y, size):
    xRange = size * 2 + 1

    positions = []
    for xIterator in range(xRange):
        xPos = x + (xIterator - size)
        yDiff = size - abs(xIterator - size)

        if xIterator == 0:
            positions.append([xPos, y])
        elif xIterator == xRange-1:
            positions.append([xPos, y])
        else:
            positions.append([xPos, y - yDiff])
            positions.append([xPos, y + yDiff])

    return positions

file = file_get_contents('input.txt')
lines = file.splitlines()
points = []
for line in lines:
    x = int(line.split(', ')[1])
    y = int(line.split(', ')[0])
    points.append([x, y])

pointsNP = np.asarray(points)
max = np.max(pointsNP, 0)
maxX = max[0]
maxY = max[1]

grid = np.zeros((maxX+1, maxY+1))

pointInfos = []
for point in pointsNP:
    grid[point[0]][point[1]] = -1
    pointInfos.append({
        "base": point,
        "points": [point],
        "infinite": False
    })

toBeClaimedLand = np.copy(grid)

areaCount = 0
for x in range(maxX):
    for y in range(maxY):
        totalDistance = 0
        for point in points:
            totalDistance += abs(x - point[0]) + abs(y - point[1])

        if totalDistance < 10000:
            areaCount += 1

print("Awnser for part 2: " + str(areaCount))