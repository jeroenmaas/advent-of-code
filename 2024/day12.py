import numpy as np

with open('day12.txt') as f:
    input = list(map(lambda a: a.strip(), f.readlines()))

def find_nearby_tiles(x, y, input):
    nearby = []
    if x > 0:
        nearby.append([x-1, y]) # left
    if x < len(input[y]) - 1:
        nearby.append([x+1, y]) # right
    if y > 0:
        nearby.append([x, y-1]) # top
    if y < len(input) - 1:
        nearby.append([x, y+1]) # bottom
    return nearby

def find_tiles_belong_to_same_group(x, y, input, group, groupedTiles):
    plantType = input[y][x]
    if groupedTiles[y][x] == 0:
        group['tiles'].append([x, y])
        groupedTiles[y][x] = 1

        nearby = find_nearby_tiles(x, y, input)
        for tile in nearby:
            if input[tile[1]][tile[0]] == plantType:
                find_tiles_belong_to_same_group(tile[0], tile[1], input, group, groupedTiles)

    return group

# step 1. Find groups
groups = []

groupedTiles = np.zeros((len(input), len(input[0])), dtype=int)

for y in range(len(input)):
    for x in range(len(input[y])):
        tileValue = input[y][x]
        if groupedTiles[y][x] == 0:
            plantType = tileValue
            group = {
                'type': tileValue,
                'tiles': []
            }
            groups.append(group)

            find_tiles_belong_to_same_group(x, y, input, group, groupedTiles)


# step 2. calculate boundaries

for group in groups:
    borderCount = 0
    for tile in group['tiles']:
        nearby = find_nearby_tiles(tile[0], tile[1], input)
        borderCount += 4 - len(nearby)

        for n in nearby:
            if input[n[1]][n[0]] != group['type']:
                borderCount += 1
    
    group['borderCount'] = borderCount


totalValue = 0
for group in groups:
    totalValue += len(group['tiles']) * group['borderCount']

# step 3. calculate final value

print('part1: ', totalValue)

# part 2. find fence parts
part2 = 0
for group in groups:
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    tilesWithDirection = {
        'top': [],
        'right': [],
        'bottom': [],
        'left': []
    }

    for tile in group['tiles']:
        for direction in directions:
            x = tile[0] + direction[0]
            y = tile[1] + direction[1]

            if y < 0:
                tilesWithDirection['top'].append(tile)
                continue

            if y >= len(input):
                tilesWithDirection['bottom'].append(tile)
                continue

            if x < 0:
                tilesWithDirection['left'].append(tile)
                continue

            if x >= len(input[y]):
                tilesWithDirection['right'].append(tile)
                continue

            if input[y][x] != group['type']:
                if direction == [0, -1]:
                    tilesWithDirection['top'].append(tile)
                elif direction == [1, 0]:
                    tilesWithDirection['right'].append(tile)
                elif direction == [0, 1]:
                    tilesWithDirection['bottom'].append(tile)
                elif direction == [-1, 0]:
                    tilesWithDirection['left'].append(tile)

    # the idea is we find the amount of fances needed for each side

    fences = 0
    for dir in ['top', 'bottom']:
        grouped = {}
        for t in tilesWithDirection[dir]:
            if t[1] not in grouped:
                grouped[t[1]] = []
            grouped[t[1]].append(t[0])

        for k, v in grouped.items():
            fences += 1
            v = sorted(v)
            for i in range(1, len(v)):
                if v[i] - v[i-1] > 1:
                    fences += 1

    for dir in ['left', 'right']:
        grouped = {}
        for t in tilesWithDirection[dir]:
            if t[0] not in grouped:
                grouped[t[0]] = []
            grouped[t[0]].append(t[1])

        for k, v in grouped.items():
            fences += 1
            v = sorted(v)
            for i in range(1, len(v)):
                if v[i] - v[i-1] > 1:
                    fences += 1

    part2 += len(group['tiles']) * fences

print('part2: ', part2)




    






