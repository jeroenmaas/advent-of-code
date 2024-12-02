with open('day10.txt') as f:
    input = sorted(list(map(lambda a: int(a), f.read().strip().split('\n'))))

def part1():
    base = 0
    diffs = {0: 0, 1: 0, 2: 0, 3: 0}
    for i in input + [max(input) + 3]:
        diffs[abs(base - i)] += 1
        base = i

    return diffs[1] * diffs[3]

print('part1: ' + str(part1()))

def part2():
    parts = [0] + input + [max(input) + 3]
    options = {}
    for i, value in enumerate(parts):
        tests = parts[i+1:i+4]
        adapters = []
        for t in tests:
            if abs(t - value) < 4:
                adapters.append(t)
        if len(adapters) > 0:
            options[value] = adapters

    max_value = list(options.values())[-1][-1]
    cache = {}
    def get_option_count_for_jolt(jolt):
        if jolt == max_value:
            return 1

        c = 0
        for o in options[jolt]:
            if o not in cache:
                cache[o] = get_option_count_for_jolt(o)
            c += cache[o]
        return c

    return get_option_count_for_jolt(0)

print('part2: ' + str(part2()))
