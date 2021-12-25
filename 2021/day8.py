import json
from itertools import combinations, permutations

# 'abc' == 'bca' becomes true
def is_same_wire(a, b):
    return len(a) == len(b) and sorted(a) == sorted(b)

with open('day8.txt') as f:
    splitted_lines = list(map(lambda a: a.replace('\n', '').split(' | '), f.readlines()))
    dashboards = []
    for splitted_line in splitted_lines:
        dashboards.append([
            splitted_line[0].split(' '),
            splitted_line[1].split(' ')
        ])

wires_by_digit = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}
items = []
for l in wires_by_digit.values():
    items.append(len(l))

c1 = 0
c2 = 0
for input, output in dashboards:
    found_wires = {
        1: '',
        4: '',
        7: '',
        8: ''
    }
    # Maps size to specific digit
    mapping = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }

    to_check_input = []
    for item in input:
        if len(item) in [2, 3, 4, 7]:
            found_wires[mapping[len(item)]] = item
        else:
            to_check_input.append(item)

    options_to_check = list(permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g']))
    possible_options = []
    for option in options_to_check:
        test_wire_setup = {
            'a': option[0],
            'b': option[1],
            'c': option[2],
            'd': option[3],
            'e': option[4],
            'f': option[5],
            'g': option[6]
        }

        possible = True
        for digit, wires in found_wires.items():
            if not possible:
                break

            expected_wires = wires_by_digit[digit] # cf
            mapped_found_wires = list(map(lambda a: test_wire_setup[a], wires))

            for wire in expected_wires:
                if wire not in mapped_found_wires:
                    possible = False
                    break
        if not possible:
            continue

        possible_options.append(test_wire_setup)

    final_option = None
    for option in possible_options:
        possible = True
        found_digits = []
        for item in input:
            mapped_item = list(map(lambda a: option[a], item))

            digit = None
            for wire_digit, wire_connections in wires_by_digit.items():
                if is_same_wire(mapped_item, wire_connections):
                    digit = wire_digit
                    break

            if digit == None:
                break
            found_digits.append(digit)

        if len(found_digits) == 10:
            final_option = option

    output_digits = ""
    for item in output:
        mapped_item = list(map(lambda a: final_option[a], item))

        digit = None
        for wire_digit, wire_connections in wires_by_digit.items():
            if is_same_wire(mapped_item, wire_connections):
                digit = wire_digit
                break

        output_digits += str(digit)

    c2 += int(output_digits)

    for item in output:
        if len(item) in [2, 3, 4, 7]:
            c1 += 1

print('part1: ', c1)
print('part2: ', c2)
