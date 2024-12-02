import math
import time

with open('day13.txt') as f:
    input = f.read().strip().split('\n')

def part1():
    startpoint = int(input[0])
    busses = []
    for b in input[1].split(','):
        if b != 'x':
            busses.append(int(b))

    nextStopByBus = {}
    for b in busses:
        previous = math.floor(startpoint / b) * b
        next = previous + b
        nextStopByBus[b] = next

    best_bus = min(nextStopByBus, key=nextStopByBus.get)
    return best_bus * (nextStopByBus[best_bus] - startpoint)

startpoint = int(input[0])
busses = {}
for offset, b in enumerate(input[1].split(',')):
    if b != 'x':
        busses[int(b)] = offset

sorted_busses = sorted(list(busses.items()), key=lambda a: a[0], reverse=False)
sorted_busses.pop(0)

def test_offset(t, base_offset):
    for b, offset in sorted_busses:
        t_offset = offset - base_offset
        to_test = t + t_offset
        if to_test % b != 0:
            return False

    return True

def part2():
    t = 0
    busses_list = list(busses.items())

    interval = busses_list.pop(0)[0]
    bus_to_check = busses_list.pop(0)
    while (True):
        t += interval
        if (t+bus_to_check[1]) % bus_to_check[0] == 0:
            interval *= bus_to_check[0]
            if len(busses_list) == 0:
                return t
            bus_to_check = busses_list.pop(0)

print('part1: ' + str(part1()))
print('part2: ' + str(part2()))
