with open('day2.txt') as f:
    input = f.readlines()
    input = list(map(lambda a: a.strip().split(' '), input))

depth = 0
horizontal = 0
for element in input:
    diff = int(element[1])
    if element[0] == 'forward':
        horizontal += diff
    elif element[0] == 'down':
        depth += diff
    elif element[0] == 'up':
        depth -= diff
    else:
        raise "unknown direction " + element[0]

print('part1: ', depth*horizontal)

depth = 0
horizontal = 0
aim = 0
for element in input:
    diff = int(element[1])
    if element[0] == 'forward':
        horizontal += diff
        depth += aim * diff
    elif element[0] == 'down':
        aim += diff
    elif element[0] == 'up':
        aim -= diff
    else:
        raise "unknown direction " + element[0]

print('part2: ', depth*horizontal)