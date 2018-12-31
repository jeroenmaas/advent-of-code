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

print(maxX)
print(maxY)
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

amountOfNewPointsAllocated = 1
currentCheck = 0
while amountOfNewPointsAllocated > 0:
    currentCheck += 1
    amountOfNewPointsAllocated = 0
    for id, info in enumerate(pointInfos):
        base = info["base"]
        pointsToCheck = generateCoordinates(base[0], base[1], currentCheck)
        for point in info["points"]:
            pointsToCheck.append([point[0] - 1, point[1]])
            pointsToCheck.append([point[0] + 1, point[1]])
            pointsToCheck.append([point[0], point[1] - 1])
            pointsToCheck.append([point[0], point[1] + 1])

        targets = np.zeros((maxX + 1, maxY + 1))
        requestedPoints = []
        for point in pointsToCheck:
            x = point[0]
            y = point[1]
            if x < 0 or x > maxX:
                continue

            if y < 0 or y > maxY:
                continue

            # We ourself are already targetting this area
            if targets[x, y]:
                continue
            targets[x, y] = 1

            valueAtLocation = toBeClaimedLand[x, y]
            # can't be claimed. Is already a base point there
            if valueAtLocation == -1:
                continue

            # can't be claimed. There is more than 1 location equally close to it.
            if valueAtLocation == -2:
                continue

            if valueAtLocation != 0 and valueAtLocation < currentCheck:
                continue

            if valueAtLocation == currentCheck:
                toBeClaimedLand[x, y] = -2
                continue

            toBeClaimedLand[x, y] = currentCheck
            requestedPoints.append(point)

        info["requestedPoints"] = requestedPoints

    for id, info in enumerate(pointInfos):
        for point in info["requestedPoints"]:
            x = point[0]
            y = point[1]
            valueAtLocation = toBeClaimedLand[x, y]
            if valueAtLocation != -2:
                info["points"].append(point)
                amountOfNewPointsAllocated += 1
                if point[0] == 0 or point[0] == maxX or point[1] == 0 or point[1] == maxY:
                    info["infinite"] = True

statsSorted = sorted(pointInfos, key=lambda r: len(r["points"]), reverse=True)
for stat in statsSorted:
    if stat["infinite"] == False:
        print("Answer for day 1 is: " + str(len(stat["points"])))
        exit()