from utils.utils import file_get_contents
import numpy as np

x = np.zeros((1200,1200))
file = file_get_contents('input.txt')

for line in file.splitlines():
    pieces = line.split(' ')
    id = pieces[0][1:]
    coordinateX = int(pieces[2].split(',')[0])
    coordinateY = int(pieces[2].split(',')[1][:-1])
    sizeX = int(pieces[3].split('x')[0])
    sizeY = int(pieces[3].split('x')[1])

    for xPos in range(sizeX):
        for yPos in range(sizeY):
            x[xPos+coordinateX][yPos+coordinateY] += 1

for line in file.splitlines():
    pieces = line.split(' ')
    id = pieces[0][1:]
    coordinateX = int(pieces[2].split(',')[0])
    coordinateY = int(pieces[2].split(',')[1][:-1])
    sizeX = int(pieces[3].split('x')[0])
    sizeY = int(pieces[3].split('x')[1])

    hasOverlay = False
    for xPos in range(sizeX):
        for yPos in range(sizeY):
            if x[xPos+coordinateX][yPos+coordinateY] > 1:
                hasOverlay = True

    if hasOverlay is False:
        print(id)




