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

powerGrouped = np.zeros((297, 297))
for x in range(297):
    for y in range(297):
        powerForCoordinate = 0
        subset = power[x:x+3, y:y+3]
        powerGrouped[x, y] = subset.sum()

maxPower = powerGrouped.max()
position = np.unravel_index(np.argmax(powerGrouped, axis=None), powerGrouped.shape)
print("answer part 1: " + str(position[0]) + "," + str(position[1]))
