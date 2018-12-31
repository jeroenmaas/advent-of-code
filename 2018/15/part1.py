from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from utils.utils import file_get_contents
import numpy as np

file = file_get_contents('input.txt')
lines = file.splitlines()

maxX = len(lines)
maxY = len(lines[0])
map = np.zeros((maxX, maxY))

def get_empty_value_for_coordinates(x, y):
    maxIndex = maxX * (maxY*2)
    index = x * (maxY * 2) + y

    return maxIndex * maxIndex + round((index / maxIndex) * maxIndex)

def getNpcAt(x, y):
    for npc in npcs:
        if npc["pos"][0] == x and npc["pos"][1] == y:
            return npc

    return None

def print_map():
    output = []
    for line in map:
        outputLine = []
        for i in line:
            if i > 0:
                outputLine.append(".")
            else:
                outputLine.append("#")
        output.append(outputLine)

    for npc in npcs:
        output[npc["pos"][0]][npc["pos"][1]] = npc["type"]

    for line in output:
        lineStr = ""
        for i in line:
            lineStr += i
        print(lineStr)

    print(npcs)

npcs = []

for x, line in enumerate(lines):
    for y, item in enumerate(line):
        if item == ".":
            map[x,y] = get_empty_value_for_coordinates(x, y)
        if item == "G" or item == "E":
            npcs.append({
                "pos": [x,y],
                "type": item,
                "health": 200
            })
        #    map[x, y] = get_empty_value_for_coordinates(x, y)
        #if item == "E":
        #    map[x, y] = get_empty_value_for_coordinates(x, y)

EntireRoundEnded = True
for i in range(1000):
    toCheckNPCs = npcs.copy()
    toCheckNPCs = sorted(toCheckNPCs, key=lambda g: get_empty_value_for_coordinates(g["pos"][0], g["pos"][1]))

    roundCompleted = False
    for npc in toCheckNPCs:
        print("npc", npc)
        if npc["health"] <= 0:
            continue

        targetsAvailable = False
        for t in npcs:
            if t["type"] != npc["type"]:
                targetsAvailable = True
                break

        if not targetsAvailable:
            EntireRoundEnded = False
            print("WARNING WARNING WE WERE DONE BEFORE ROUND END")
            continue

        x = npc["pos"][0]
        y = npc["pos"][1]
        type = npc["type"]

        nearbyNpcs = []
        nearbyNpcs.append(getNpcAt(x, y-1))
        nearbyNpcs.append(getNpcAt(x - 1, y))
        nearbyNpcs.append(getNpcAt(x + 1, y))
        nearbyNpcs.append(getNpcAt(x, y + 1))

        targets = []
        for nearbyNpc in nearbyNpcs:
            if not nearbyNpc:
                continue
            if nearbyNpc["type"] != type:
                targets.append(nearbyNpc)

        print("targets: ", targets)

        target = None
        if len(targets) > 1:
            targetOptions = sorted(targets,
                                   key=lambda t: t["health"])

            if targetOptions[0]["health"] == targetOptions[1]["health"]:
                maxHealth = targetOptions[0]["health"]
                targetsWithSameHealth = []
                for o in targetOptions:
                    if o["health"] == maxHealth:
                        targetsWithSameHealth.append(o)

                targetsWithSameHealth = sorted(targetsWithSameHealth,
                                       key=lambda t: get_empty_value_for_coordinates(t["pos"][0], t["pos"][1]))

                print(targetsWithSameHealth)
                target = targetsWithSameHealth[0]
            else:
                target = targetOptions[0]

        elif len(targets) == 1:
            target = targets[0]
        else:
            # Since we have no targets next to use we attempt to find a target and move
            targetOptions = []
            for targetNPC in npcs:
                if targetNPC["type"] != type:
                    toTest = map.copy()
                    toTest[x, y] = get_empty_value_for_coordinates(x, y)
                    toTest[targetNPC["pos"][0], targetNPC["pos"][1]] = get_empty_value_for_coordinates(targetNPC["pos"][0], targetNPC["pos"][1])
                    grid = Grid(matrix=toTest)
                    start = grid.node(y, x)

                    end = grid.node(targetNPC["pos"][1], targetNPC["pos"][0])
                    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
                    path, runs = finder.find_path(start, end, grid)

                    if len(path) > 0:
                        d = path[-2]

                        maxIndex = maxX * (maxY * 2)
                        optionValue = len(path) + (1 - 1 / get_empty_value_for_coordinates(d[1], d[0]))
                        targetOptions.append({
                            "npc": targetNPC,
                            "path": path,
                            "optionValue": optionValue
                        })
            if len(targetOptions) > 0:
                targetOptions = sorted(targetOptions,
                                     key=lambda t: t["optionValue"])

                if len(targetOptions) > 1 and targetOptions[0]["optionValue"] == targetOptions[1]["optionValue"]:
                    bestOptionValue = targetOptions[0]["optionValue"]
                    optionsWithSameOptionValue = []

                    for o in targetOptions:
                        if o["optionValue"] == bestOptionValue:
                            optionsWithSameOptionValue.append(o)

                    targetOptions = sorted(optionsWithSameOptionValue,
                                     key=lambda t: t["npc"]["health"])

                # Alright we have set our target. Lets move
                nextMove = targetOptions[0]["path"][1]
                nextMoveX = nextMove[1]
                nextMoveY = nextMove[0]
                map[x, y] = get_empty_value_for_coordinates(x, y)
                map[nextMoveX, nextMoveY] = 0
                npc["pos"] = [nextMoveX, nextMoveY]

                if len(targetOptions[0]["path"]) == 3:
                    target = targetOptions[0]["npc"]

        print("ATTACK:", target)
        if target:
            target["health"] = target["health"] - 3
            if target["health"] <= 0:
                map[target["pos"][0], target["pos"][1]] = get_empty_value_for_coordinates(target["pos"][0], target["pos"][1])
                npcs.remove(target)
                print("KILL")

    GCount = 0
    ECount = 0
    for npc in npcs:
        if npc["type"] == "G":
            GCount += 1
        elif npc["type"] == "E":
            ECount += 1


    print(i+1)
    print_map()
    if GCount == 0 or ECount == 0:
        print("We are done after " + str(i) + " rounds")

        remainingHealthPoints = 0
        for npc in npcs:
            remainingHealthPoints += npc["health"]

        print_map()

        rounds = i
        if EntireRoundEnded:
            rounds += 1

        print(remainingHealthPoints)
        print(rounds)

        print("Part 1 answer: " + str(remainingHealthPoints*rounds))
        exit()

# grid = Grid(matrix=map)
#
# start = grid.node(1, 1)
# end = grid.node(5, 5)
#
# finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
# path, runs = finder.find_path(start, end, grid)
#
# print(path)
# print('operations:', runs, 'path length:', len(path))
