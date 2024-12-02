with open('day1.txt') as f:
    input = f.readlines()
    input = list(map(lambda a: int(a.strip()), input))

def part1(input):
    for i in input:
        for y in input:
            if y + i == 2020:
                return y * i

def part2(input):
    for i in input:
        for y in input:
            for z in input:
                if y + i + z == 2020:
                    return y * i * z

print('part1: ' + str(part1(input)))
print('part2: ' + str(part2(input)))
