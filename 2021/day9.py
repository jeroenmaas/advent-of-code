import json
import math
from itertools import combinations, permutations

def get_item_at_coordinate(cave, x, y):
    if y < 0:
        return None
    if y >= len(cave):
        return None
    if x < 0:
        return None
    if x >= len(cave[0]):
        return None

    return cave[y][x]

def to_hash(x, y):
    return str(x) + '_' + str(y)

def expand_basin_if_possible(cave, basin, x, y, processed_points):
    connected_pieces = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]

    for lookx, looky in connected_pieces:
        hash = to_hash(lookx, looky)
        if hash in basin or hash in processed_points:
            continue

        start_value = get_item_at_coordinate(cave, lookx, looky)
        if start_value is None or start_value == 9:
            continue

        basin.append(hash)
        processed_points.append(hash)
        expand_basin_if_possible(cave, basin, lookx, looky, processed_points)

with open('day9.txt') as f:
    lines = f.readlines()
    lines = list(map(lambda a: a.strip(), lines))

    cave = []
    for line in lines:
        cave.append(list(map(lambda a: int(a), line)))



c1 = 0
for x in range(len(cave[0])):
    for y in range(len(cave)):
        my_value = get_item_at_coordinate(cave, x, y)
        connected_pieces = [
            get_item_at_coordinate(cave, x+1, y),
            get_item_at_coordinate(cave, x-1, y),
            get_item_at_coordinate(cave, x, y+1),
            get_item_at_coordinate(cave, x, y-1),
        ]

        lowest_point = True
        for c in connected_pieces:
            if c is not None and c <= my_value:
                lowest_point = False
                break

        if lowest_point:
            c1 += (my_value + 1)

print('part1: ', c1)


basins = []
processed_points = []
found_basin = True
while found_basin:
    found_basin = False
    for x in range(len(cave[0])):
        for y in range(len(cave)):
            hash = to_hash(x, y)
            if hash in processed_points:
                continue

            start_value = get_item_at_coordinate(cave, x, y)
            if start_value is None or start_value == 9:
                continue

            found_basin = True
            basin = []
            basin.append(hash)
            processed_points.append(hash)
            expand_basin_if_possible(cave, basin, x, y, processed_points)
            basins.append(basin)
            # Not that we are here we can continue to look around us until we have found the entire basin



basin_sizes = []
for basin in basins:
    basin_sizes.append(len(basin))

basin_sizes.sort(reverse=True)

print('part2: ', math.prod(basin_sizes[:3]))

