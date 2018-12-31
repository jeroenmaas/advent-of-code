from utils.utils import file_get_contents
import numpy as np

def get_power(x, y, serial):
    rackId = x + 10
    powerLevel = rackId * y
    powerWithSerial = powerLevel + serial
    multipliedRackId = powerWithSerial * rackId
    hunderedDigit = int(str(multipliedRackId)[-3])
    return hunderedDigit - 5

file = file_get_contents('input.txt')
serialNumber = int(file.splitlines()[0])

power = np.zeros((300,300))

for x in range(300):
    for y in range(300):
        power[x, y] = get_power(x, y, serialNumber)

maxPowerPerSize = np.zeros(300)
largestCoordinatesPerSize = []
for s in range(300):
    print(s)
    powerGrouped = np.zeros((300 - s, 300 - s))
    for x in range(300 - s):
        for y in range(300 - s):
            powerForCoordinate = 0
            subset = power[x:x+s, y:y+s]
            powerGrouped[x, y] = subset.sum()

    maxPower = powerGrouped.max()
    position = np.unravel_index(np.argmax(powerGrouped, axis=None), powerGrouped.shape)
    maxPowerPerSize[s] = maxPower
    largestCoordinatesPerSize.append(position)

bestSize = maxPowerPerSize.argmax()
pos = largestCoordinatesPerSize[bestSize]
print("part 2 answer: " + str(pos[0]) + "," + str(pos[1]) + "," + str(bestSize))