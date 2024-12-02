with open('day6.txt') as f:
    input = list(map(lambda a: a.split('\n'), f.read().strip().split('\n\n')))

unique_count = 0
unique_count2 = 0
for g in input:
    unique_count += len(set("".join(g)))

    count_by_char = {}
    for p in g:
        for a in p:
            if a not in count_by_char:
                count_by_char[a] = 0
            count_by_char[a] += 1

    for key in count_by_char.keys():
        if count_by_char[key] == len(g):
            unique_count2 += 1

print('part1: ' + str(unique_count))
print('part2: ' + str(unique_count2))
