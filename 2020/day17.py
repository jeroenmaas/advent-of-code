import json

with open('day17.txt') as f:
    input = f.read().strip().split('\n')

def part1():
    def gen_lookup(x, y, z):
        return '_'.join([str(x), str(y), str(z)])

    def get_coordinates(k: str):
        return list(map(lambda a: int(a), k.split('_')))

    def get_neighbours(xOrigin, yOrigin, zOrigin, cubes):
        neighbours = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for z in [-1, 0, 1]:
                    if x == 0 and y == 0 and z == 0:
                        continue
                    x2 = x + xOrigin
                    y2 = y + yOrigin
                    z2 = z + zOrigin
                    lookup = gen_lookup(x2, y2, z2)
                    if lookup in cubes and cubes[lookup] == True:
                        neighbours.append([x2, y2, z2])

        return neighbours

    cubes = {}
    for x in range(len(input[0])):
        for y in range(len(input)):
            if input[y][x] == '#':
                cubes[gen_lookup(x, y, 0)] = True

    for i in range(6):
        xpositions = []
        ypositions = []
        zpositions = []
        for k in cubes.keys():
            x, y, z = get_coordinates(k)
            xpositions.append(x)
            ypositions.append(y)
            zpositions.append(z)

        new_cubes = json.loads(json.dumps(cubes))
        for x in range(min(xpositions) - 2, max(xpositions) + 2):
            for y in range(min(ypositions) - 2, max(ypositions) + 2):
                for z in range(min(zpositions) - 2, max(zpositions) + 2):
                    l = gen_lookup(x, y, z)
                    neighbours = get_neighbours(x, y, z, cubes)
                    if l in cubes and cubes[l] == True:
                        # print('found cube!')
                        if not (len(neighbours) == 2 or len(neighbours) == 3):
                            del new_cubes[l]
                    else:
                        if len(neighbours) == 3:
                            new_cubes[l] = True
                        continue
        cubes = new_cubes

    return len(cubes)

def part2():
    def gen_lookup(x, y, z, w):
        return '_'.join([str(x), str(y), str(z), str(w)])

    def get_coordinates(k: str):
        return list(map(lambda a: int(a), k.split('_')))

    def get_neighbours(xOrigin, yOrigin, zOrigin, wOrigin, cubes):
        neighbours = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for z in [-1, 0, 1]:
                    for w in [-1, 0, 1]:
                        if x == 0 and y == 0 and z == 0 and w == 0:
                            continue
                        x2 = x+xOrigin
                        y2 = y+yOrigin
                        z2 = z+zOrigin
                        w2 = w+wOrigin
                        lookup = gen_lookup(x2, y2, z2, w2)
                        if lookup in cubes and cubes[lookup] == True:
                            neighbours.append([x2, y2, z2, w2])
        return neighbours

    cubes = {}
    for x in range(len(input[0])):
        for y in range(len(input)):
            if input[y][x] == '#':
                cubes[gen_lookup(x, y, 0, 0)] = True

    for i in range(6):
        xpositions = []
        ypositions = []
        zpositions = []
        wpositions = []
        for k in cubes.keys():
            x, y, z, w = get_coordinates(k)
            xpositions.append(x)
            ypositions.append(y)
            zpositions.append(z)
            wpositions.append(w)

        new_cubes = json.loads(json.dumps(cubes))
        for x in range(min(xpositions)-2, max(xpositions)+2):
            for y in range(min(ypositions)-2, max(ypositions)+2):
                for z in range(min(zpositions)-2, max(zpositions)+2):
                    for w in range(min(wpositions) - 2, max(wpositions) + 2):
                        l = gen_lookup(x, y, z, w)
                        neighbours = get_neighbours(x, y, z, w, cubes)
                        if l in cubes and cubes[l] == True:
                            #print('found cube!')
                            if not (len(neighbours) == 2 or len(neighbours) == 3):
                                del new_cubes[l]
                        else:
                            if len(neighbours) == 3:
                                new_cubes[l] = True
                            continue
        cubes = new_cubes

    return len(cubes)

print('part1: ' + str(part1()))
print('part2: ' + str(part2()))
