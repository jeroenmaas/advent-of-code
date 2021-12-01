with open('day1.txt') as f:
    input = f.readlines()
    input = list(map(lambda a: int(a.strip()), input))

larger_count = 0
for i in range(1, len(input)):
    prev = input[i-1]
    curr = input[i]
    if curr > prev:
        larger_count += 1

print('part1: ', larger_count)

larger_count = 0
for i in range(3, len(input)):
    prev_values = [input[i-3], input[i-2], input[i-1]]
    curr_values = [input[i-2], input[i-1], input[i]]

    if sum(curr_values) > sum(prev_values):
        larger_count += 1

print('part2: ', larger_count)