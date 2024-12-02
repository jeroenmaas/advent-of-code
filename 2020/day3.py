import math

with open('day3.txt') as f:
    input = f.read().split('\n')


def countTrees(input, stepX, stepY):
    maxY = len(input)
    maxX = len(input[0])

    x = 0
    y = 0
    c = 0

    while maxY > (y + 2):
        y += stepY
        x += stepX

        xIndex = x - math.floor((x + 1) / maxX) * maxX

        if input[y][xIndex] == "#":
            c += 1

    return c

print('part1: ' + str(countTrees(input, stepX=1, stepY=2)))

c = 1
for item in [[1, 1], [3, 1], [5, 1], [7,1], [1,2]]:
    c *= countTrees(input, stepX=item[0], stepY=item[1])
print('part2: ' + str(c))
