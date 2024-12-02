with open('day3.txt') as f:
    input = f.readlines()
    input = list(map(lambda a: list(a.strip()), input))


detected_symbols = []
detected_symbol_locations = set()
detected_item = []
parts = []
for x in range(len(input)):
    for y in range(len(input[x])):
        if input[x][y].isdigit():
            detected_item.append(input[x][y])

            to_check = [
                (x-1, y),
                (x+1, y),
                (x, y-1),
                (x, y+1),
                (x - 1, y - 1),
                (x - 1, y + 1),
                (x + 1, y - 1),
                (x + 1, y + 1),
            ]

            for x2, y2 in to_check:
                if x2 < 0 or x2 >= len(input):
                    continue
                if y2 < 0 or y2 >= len(input[x2]):
                    continue
                if input[x2][y2].isdigit():
                    continue
                if input[x2][y2] == '.':
                    continue

                detected_symbols.append(input[x2][y2])
                detected_symbol_locations.add((str(x2), str(y2)))
        else:
            if len(detected_item) >= 1:
                parts.append([detected_item, detected_symbols, detected_symbol_locations])
            detected_item = []
            detected_symbols = []
            detected_symbol_locations = set()

s = 0
for p in parts:
    if len(p[1]) > 0:
        s += int(''.join(p[0]))
print('part1: ', s)

parts_by_symbol_location = {}
for p in parts:
    for symbol_location in p[2]:
        if p[1][0] != '*':
            continue
        lookup = '-'.join(symbol_location)

        if lookup not in parts_by_symbol_location:
            parts_by_symbol_location[lookup] = []
        parts_by_symbol_location[lookup].append(p)

part2 = 0
for loc, items in parts_by_symbol_location.items():
    if(len(items) == 2):
        part2 += int(''.join(items[0][0])) * int(''.join(items[1][0]))

print('part2: ',part2)

