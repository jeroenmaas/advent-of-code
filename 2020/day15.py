with open('day15.txt') as f:
    input = list(map(lambda a: int(a), f.read().strip().split(',')))

def find_result(max_turn_count):

    turns = []
    numberCache = {} # keeps a cache with index == number and value == array of last time spoken

    turn = 1
    previous_number = None
    for i, number in enumerate(input):
        turn = i + 1
        turns.append(number)
        previous_number = number
        if number not in numberCache:
            numberCache[number] = []
        numberCache[number].append(turn)

    while(turn != max_turn_count):
        turn += 1
        if previous_number not in numberCache.keys():
            new_number = 0
        else:
            c = numberCache[previous_number]
            if len(c) == 1:
                new_number = 0
            else:
                last_two_numbers = c[-2:]
                new_number = last_two_numbers[1] - last_two_numbers[0]

        previous_number = new_number
        if new_number not in numberCache:
            numberCache[new_number] = []
        numberCache[new_number].append(turn)

    return previous_number

print('part1: ' + str(find_result(2020)))
print('part2: ' + str(find_result(30000000)))
