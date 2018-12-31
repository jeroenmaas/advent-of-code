import re
import numpy as np
from utils.utils import file_get_contents

file = file_get_contents('input.txt')
lines = file.splitlines()

infos = []

for idx, line in enumerate(lines):
    matches = re.findall('<(.*?)>', line)
    position = matches[0].split(', ')
    positionX = int(position[0])
    positionY = int(position[1])
    speed = matches[1].split(', ')
    speedX = int(speed[0])
    speedY = int(speed[1])
    info ={
        "posX": positionX,
        "posY": positionY,
        "speedX": speedX,
        "speedY": speedY
    }
    infos.append(info)

distanceToZeroStats = np.zeros(15000)
for i in range(15000):
    distanceToZero = 0
    for info in infos:
        distanceX = info["posX"] + info["speedX"]*i
        distanceY = info["posY"] + info["speedY"]*i
        distanceToZero += abs(distanceX) + abs(distanceY)
    distanceToZeroStats[i] = distanceToZero

bestSeconds = distanceToZeroStats.argmin()

for i in range(100):
    toTest = bestSeconds + (50 - i)

    w, h = 600, 600
    display = np.zeros((h, w, 3), dtype=np.uint8)
    for info in infos:
        distanceX = info["posX"] + info["speedX"] * toTest
        distanceY = info["posY"] + info["speedY"] * toTest
        display[distanceX, distanceY] = [255, 255, 255]

    from PIL import Image
    import numpy as np

    img = Image.fromarray(display, 'RGB')
    img.save('build/' + str(toTest) + '.png')
    #img.show()
