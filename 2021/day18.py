import json
import math
from copy import deepcopy
from itertools import combinations

LEFT_DIR = 0
RIGHT_DIR = 1

def respr_as_aoc(snailfish_number):
    return str(snailfish_number).replace(' ', '')

def print_as_oac(snailfish_number):
    print(respr_as_aoc(snailfish_number))

def addition(part1, part2):
    return [part1, part2]

def get_value_at_location(parent, location):
    final = parent
    for y in location:
        final = final[y]

    return final

def find_part(snailfish_number, location_origin, dir):
    # We make a copy so its safe to mutate the data
    location = location_origin.copy()
    for i in reversed(range(len(location))):
        if location[i] == dir:
            # Bit of a weird hack for right (1). But say we have [0, 1, 1, 1] This should got to [1, 0, 0, 0]
            # If we have [0, 0, 1, 1] we should get [0, 1, 0, 0]
            if dir == 1:
                location[i] = 0
            else:
                location[i] = 1
            continue

        location[i] = dir
        for i in range(1, len(location)+1):
            check_loc = location[0:i]
            v = get_value_at_location(snailfish_number, check_loc)
            if not isinstance(v, list):
                return get_value_at_location(snailfish_number, check_loc[:-1]), check_loc[-1]

        final_parent = get_value_at_location(snailfish_number, location)
        if isinstance(final_parent, list) and not isinstance(final_parent[0 if dir == 1 else 1], list):
            return final_parent, 0 if dir == 1 else 1

    return None, None

def find_left_part(snailfish_number, location):
    return find_part(snailfish_number, location, LEFT_DIR)

def find_right_part(snailfish_number, location):
    return find_part(snailfish_number, location, RIGHT_DIR)

def check_action(snailfish_number, snailfish_number_part, location, type):
    index = len(location)
    if index == 4 and type == 'explode':
        left_parent, ldir = find_left_part(snailfish_number, location)
        right_parent, rdir = find_right_part(snailfish_number, location)

        if left_parent:
            left_parent[ldir] = left_parent[ldir] + snailfish_number_part[LEFT_DIR]
        if right_parent:
            right_parent[rdir] = right_parent[rdir] + snailfish_number_part[RIGHT_DIR]
        get_value_at_location(snailfish_number, location[:-1])[location[-1]] = 0
        return snailfish_number

    if index > 4:
        raise 'We should never have an index of 5 or larger'

    for dir in [LEFT_DIR, RIGHT_DIR]:
        if type == 'split' and not isinstance(snailfish_number_part[dir], list) and snailfish_number_part[dir] >= 10:
            dvalue = snailfish_number_part[dir]
            new_value = [math.floor(dvalue / 2), math.ceil(dvalue / 2)]
            get_value_at_location(snailfish_number, location)[dir] = new_value
            return snailfish_number

        if isinstance(snailfish_number_part[dir], list):
            result = check_action(snailfish_number, snailfish_number_part[dir], location + [dir], type)
            if result:
                return result


def magnitude_step(snailfish_number, snailfish_number_part, location):
    if not isinstance(snailfish_number_part, list):
        return snailfish_number_part

    if not isinstance(snailfish_number_part[0], list) and not isinstance(snailfish_number_part[1], list):
        new_value = snailfish_number_part[0] * 3 + snailfish_number_part[1] * 2
        if len(location) == 0:
            return new_value
        get_value_at_location(snailfish_number, location[:-1])[location[-1]] = new_value
        return snailfish_number_part[0] * 3 + snailfish_number_part[1] * 2

    magnitude_step(snailfish_number, snailfish_number_part[0], location + [0])
    magnitude_step(snailfish_number, snailfish_number_part[1], location + [1])
    return None

def calculate_magnitude(snailfish_number):
    while True:
        result = magnitude_step(snailfish_number, snailfish_number, [])
        if result:
            return result

with open('day18.txt') as f:
    input = list(map(lambda a: json.loads(a), f.readlines()))

snailfish_number = input[0]

for item in input[1:]:
    snailfish_number = addition(snailfish_number, item)

    final_result = snailfish_number
    while True:
        result = check_action(snailfish_number, snailfish_number, [], 'explode')
        if not result:
            result = check_action(snailfish_number, snailfish_number, [], 'split')
            if not result:
                break
    snailfish_number = final_result

print('part1:', calculate_magnitude(snailfish_number))

largest_magnitude = 0
for combination in list(combinations(input, 2)):
    for reversd in [False, True]:
        if reversd:
            snailfish_number = addition(deepcopy(combination[1]), deepcopy(combination[0]))
        else:
            snailfish_number = addition(deepcopy(combination[0]), deepcopy(combination[1]))

        final_result = snailfish_number
        while True:
            result = check_action(snailfish_number, snailfish_number, [], 'explode')
            if not result:
                result = check_action(snailfish_number, snailfish_number, [], 'split')
                if not result:
                    break
        snailfish_number = final_result
        largest_magnitude = max(calculate_magnitude(snailfish_number), largest_magnitude)

print('part2: ', largest_magnitude)