from utils.utils import file_get_contents
import numpy as np

file = file_get_contents('input.txt')
lines = file.splitlines()

trackOptions = {
    " ": 0,
    "|": 1,
    "-": 2,
    "+": 3,
    "/": 4,
    "\\": 5,
    ">": 2,
    "<": 2,
    "^": 1,
    "v": 1
}

# important! this is ordered clockwise
cartDirections = {
    "^": "up",
    ">": "right",
    "v": "down",
    "<": "left"
}

maxX = len(lines)
minX = 0
maxY = 0
for line in lines:
    if len(line) > maxY:
        maxY = len(line)
minY = 0

carts = []

map = np.zeros((maxX, maxY))
for x, line in enumerate(lines):
    for y, item in enumerate(line):
        value = trackOptions[item]
        map[x, y] = value

        if item in cartDirections:
            carts.append({
                "direction": cartDirections[item],
                "position": [x, y],
                "nextTurn": "left"
            })

def print_visual_map(map, carts):
    output = []
    for line in map:
        outputLine = ""
        for item in line:
            for tOption, value in trackOptions.items():
                if value == item:
                    outputLine += tOption
                    break
        output.append(outputLine)
    for cart in carts:
        direction = None
        for k, value in cartDirections.items():
            if value == cart["direction"]:
                direction = k
        x = cart["position"][0]
        y = cart["position"][1]
        output[x] = output[x][:y] + direction + output[x][y + 1:]

    for line in output:
        print(line)


def continueXTimesInArray(array, currentIndex, continueTimes):
    nextIndex = currentIndex
    for i in range(continueTimes):
        if nextIndex < len(array) - 1:
            nextIndex += 1
        else:
            nextIndex = 0

    return array[nextIndex]


# print_visual_map(map, carts)
for i in range(5000):
    for cart in carts:
        dir = cart["direction"]

        if dir == "right":
            cart["position"][1] += 1
        elif dir == "left":
            cart["position"][1] -= 1
        elif dir == "up":
            cart["position"][0] -= 1
        elif dir == "down":
            cart["position"][0] += 1

        track = map[cart["position"][0], cart["position"][1]]
        if track == 0:
            print(cart["position"])
            print_visual_map(map, carts)
            exit()

        if track == 4:  # /
            if dir == "left":
                dir = "down"
            elif dir == "up":
                dir = "right"
            elif dir == "down":
                dir = "left"
            elif dir == "right":
                dir = "up"
        elif track == 5:  # \
            if dir == "left":
                dir = "up"
            elif dir == "up":
                dir = "left"
            elif dir == "down":
                dir = "right"
            elif dir == "right":
                dir = "down"
        elif track == 3:  # +
            options = list(cartDirections.values())
            indexOfOption = options.index(dir)
            if cart["nextTurn"] == "left":
                dir = continueXTimesInArray(options, indexOfOption, 3)
                cart["nextTurn"] = "straight"
            elif cart["nextTurn"] == "straight":
                cart["nextTurn"] = "right"
            elif cart["nextTurn"] == "right":
                dir = continueXTimesInArray(options, indexOfOption, 1)
                cart["nextTurn"] = "left"

        cart["direction"] = dir

        positions = []
        for cart in carts:
            if cart["position"] in positions:
                print("colision detected: " + str(cart["position"][1]) + "," + str(cart["position"][0]))
                print_visual_map(map, carts)
                exit()
            else:
                positions.append(cart["position"])


