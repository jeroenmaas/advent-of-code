import copy

with open('day3.txt') as f:
    input = f.readlines()
    input = list(map(lambda a: str(a.strip()), input))

def most_frequent(List):
    return max(set(List), key = List.count)

items_by_position = {}
for line in input:
    for i, item in enumerate(line):
        if i not in items_by_position:
            items_by_position[i] = []
        items_by_position[i].append(int(item))

most_freq_line = ""
least_freq_line = ""

for i, items in items_by_position.items():
    most_freq = most_frequent(items)
    most_freq_line += str(most_frequent(items))
    least_freq_line += "0" if most_freq == 1 else "1"

print('part1: ', int(most_freq_line, 2) * int(least_freq_line, 2))

def find_rating(a, type):
    filtered = copy.deepcopy(a)
    search = ''
    for i in range(len(filtered)):
        values_on_position = []
        for line in filtered:
            values_on_position.append(int(line[i]))

        # We have no clear winner
        if sum(values_on_position) == len(values_on_position) / 2:
            search += '1' if type == 'oxygen' else '0'
        else:
            new_item = most_frequent(values_on_position)
            if type == 'co2':
                new_item = 0 if new_item == 1 else 1
            search += str(new_item)

        filtered = list(filter(lambda a: a.startswith(search), filtered))
        if len(filtered) == 1:
            return filtered[0]

print('part2: ', int(find_rating(input, 'oxygen'), 2) * int(find_rating(input, 'co2'), 2))