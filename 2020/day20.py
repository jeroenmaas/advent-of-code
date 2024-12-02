import json
import math

import numpy as np

with open('day20.txt') as f:
    tiles_input = list(map(lambda a: a.split('\n'), f.read().strip().split('\n\n')))


# Because i don't know the amount of unique positions i'll just rotate
def generate_options(tile_parts):
    options = []

    tile_parts_np = np.array(list(map(lambda a: list(a), tile_parts)))
    for i in range(4):
        tile_parts_np = np.rot90(tile_parts_np)
        options.append(tile_parts_np)

        r = np.array(list(reversed(list(tile_parts_np))))
        options.append(r)

    return options


def generate_borders(tile_parts):
    borders = []
    borders.append(tile_parts[0])
    right = []
    for i in tile_parts:
        right.append(i[-1])
    borders.append(right)
    borders.append(tile_parts[-1])
    left = []
    for i in tile_parts:
        left.append(i[0])
    borders.append(left)
    return borders


def convert_border_to_value(border):
    value = 0
    for i, b in enumerate(reversed(border)):
        if b == True:
            value += pow(2, i)
    return value


def print_option(option):
    for line in option:
        print(''.join(map(lambda a: '#' if a else '.', line)))


def remove_border(option):
    n = []
    for l in option[1:-1]:
        n.append(l[1:-1])
    return n


def check_neighbours(map, x, y, border_option):
    inverse_direction = [2, 3, 0, 1]

    # check top, right, bottom, left
    for i, (yoffset, xoffset) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
        xcheck = x + xoffset
        ycheck = y + yoffset
        try:
            border = map[ycheck][xcheck]
            if border is not None and border[inverse_direction[i]] != border_option[i]:
                return False
        except:
            pass
    return True


tiles = {}
for i in tiles_input:
    id = int(i[0].replace('Tile ', '').replace(':', ''))
    tile_parts = list(map(lambda a: list(map(lambda b: b == '#', a)), i[1:]))
    options = generate_options(tile_parts)

    borders_options = list(map(lambda a: list(map(lambda b: convert_border_to_value(b), generate_borders(a))), options))
    tiles[id] = {
        'options': options,
        'borders_options': borders_options
    }

size = int(math.sqrt(len(tiles)))
a = np.zeros((size, size))

m = a.tolist()
for x in range(size):
    for y in range(size):
        m[y][x] = None

options = []
for x in range(size):
    for y in range(size):
        if x == 0 and y == 0:
            for id, t in tiles.items():
                for bo in t['borders_options']:
                    new_map = json.loads(json.dumps(m))
                    new_map[0][0] = bo

                    options.append({'map': new_map, 'ids': [id]})
        else:
            previous_options = options
            options = []
            for p in previous_options:
                for id, t in tiles.items():
                    if id in p['ids']:
                        continue

                    for bo in t['borders_options']:
                        if check_neighbours(p['map'], x, y, bo):
                            new_map = json.loads(json.dumps(p['map']))
                            new_map[y][x] = bo
                            ids = json.loads(json.dumps(p['ids']))
                            ids.append(id)
                            options.append({'map': new_map, 'ids': ids})

ids = options[0]['ids']

corners = []
corners.append(ids[0])
corners.append(ids[-1])
corners.append(ids[size - 1])
corners.append(ids[size * size - size])

output = 1
for c in corners:
    output *= c

print('part1: ', output)

full_maps = []
for o in options:
    ids = o['ids']
    map2 = o['map']
    new_map = np.zeros((size, size)).tolist()
    i = 0
    for x in range(size):
        for y in range(size):
            border_index = tiles[ids[i]]['borders_options'].index(map2[y][x])
            new_map[y][x] = remove_border(tiles[ids[i]]['options'][border_index])
            i += 1

    new_map2 = []
    for y, pieces in enumerate(new_map):
        lines = list(map(lambda a: [], range(len(pieces[0]))))
        for piece in pieces:
            for y, values in enumerate(piece):
                for v in values:
                    lines[y].append(v)
        new_map2.extend(lines)

    full_maps.append(new_map2)

flatten = lambda t: [item for sublist in t for item in sublist]

d_search = []
d_search.append('                  # ')
d_search.append('#    ##    ##    ###')
d_search.append(' #  #  #  #  #  #   ')
d_search_flat = flatten(d_search)
d_search_value = convert_border_to_value(list(map(lambda b: b == '#', d_search_flat)))
d_len = len(d_search[0])

for i, m in enumerate(full_maps):
    sea_monsters = 0
    for x in range(len(m[0])):
        for y in range(len(m)):
            try:
                test = []
                for i in range(len(d_search)):
                    test.append(m[y + i][x:x + d_len])

                test_flattend = flatten(test)
                if len(test_flattend) != 60:
                    continue

                test_value = convert_border_to_value(test_flattend)
                if test_value & d_search_value == d_search_value:
                    sea_monsters += 1
            except:
                pass

    if sea_monsters > 0:
        total_count = np.sum(m)
        print('part2: ', total_count - sea_monsters * 15)
