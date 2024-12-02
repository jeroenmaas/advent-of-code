import json

with open('day11.txt') as f:
    main_map = list(map(lambda s: list(s), f.read().split('\n')))


maxY = len(main_map)
maxX = len(main_map[0])

def print_map(map):
    for y in map:
        line = ""
        for s in y:
            line += s

        print(line)

def get_direct_neighbors(main_map, x, y):
    to_test = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1]
    ]

    neighbors = []
    for (x_offset, y_offset) in to_test:
        x_to_test = x + x_offset
        y_to_test = y + y_offset

        if x_to_test < 0 or y_to_test < 0:
            continue

        try:
            neighbors.append(main_map[y_to_test][x_to_test])
        except:
            pass

    return neighbors

def get_los_neighbors(main_map, x, y):
    to_test = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1]
    ]

    neighbors = []


    for (x_offset, y_offset) in to_test:
        xbase = x
        ybase = y
        while(True):
            xbase += x_offset
            ybase += y_offset

            if xbase < 0 or ybase < 0:
                break

            try:
                if main_map[ybase][xbase] == '.':
                    continue

                neighbors.append(main_map[ybase][xbase])
                break
            except:
                break

    return neighbors

def step(main_map):
    new_map = json.loads(json.dumps(main_map))

    for y, line in enumerate(main_map):
        for x, i in enumerate(line):
            if i == '.':
                continue

            neighbours = get_direct_neighbors(main_map, x, y)
            taken_seats = sum(map(lambda s : s == '#', neighbours))
            if i == 'L' and taken_seats == 0:
                new_map[y][x] = '#'
            elif i == '#' and taken_seats >= 4:
                new_map[y][x] = 'L'
    return new_map

def step2(main_map):
    new_map = json.loads(json.dumps(main_map))

    for y, line in enumerate(main_map):
        for x, i in enumerate(line):
            if i == '.':
                continue

            neighbours = get_los_neighbors(main_map, x, y)
            taken_seats = sum(map(lambda s : s == '#', neighbours))
            if i == 'L' and taken_seats == 0:
                new_map[y][x] = '#'
            elif i == '#' and taken_seats >= 5:
                new_map[y][x] = 'L'
    return new_map

def part1(main_map):
    current_count = -1
    last_count = 0
    while(current_count != last_count):
        last_count = current_count
        main_map = step(main_map)

        c = 0
        for yLine in main_map:
            for seat in yLine:
                if seat == '#':
                    c += 1
        current_count = c

    return current_count

def part2(main_map):
    current_count = -1
    last_count = 0
    while(current_count != last_count):
        last_count = current_count
        main_map = step2(main_map)

        c = 0
        for yLine in main_map:
            for seat in yLine:
                if seat == '#':
                    c += 1
        current_count = c

    return current_count

print('part1: ' + str(part1(main_map)))
print('part2: ' + str(part2(main_map)))
