with open('day9.txt') as f:
    input = list(map(lambda a: int(a), f.read().strip().split('\n')))

def part1():
    #37 failed because preablesize != 25
    preablesize = 25

    i = 0
    while(True):
        preamble = input[i:(i+preablesize)]
        value = input[i+preablesize]

        possible_sums = []
        for y in preamble:
            for z in preamble:
                if y != z:
                    possible_sums.append(y+z)

        if value not in possible_sums:
            return value

        i += 1

def part2(partToFind):
    parts = 2
    while(True):
        for pos, item in enumerate(input):
            values = []
            invalid = False
            for p in range(parts):
                if pos+p > len(input)-1:
                    invalid = True
                    break
                values.append(input[pos+p])
            if not invalid and partToFind == sum(values):
                return min(values) + max(values)
        parts += 1

part1value = part1()
print('part1: ' + str(part1value))
print('part2: ' + str(part2(part1value)))

