with open('day1.txt') as f:
    input = f.readlines()
    input = list(map(lambda a: a.strip().split('   '), input))

left = sorted(list(map(lambda a: int(a[0]), input)))
right = sorted(list(map(lambda a: int(a[1]), input)))

offsets = []
for i in range(0, len(left)):
    offsets.append(abs(left[i] - right[i]))
        
print('part1: ', sum(offsets))

left = list(map(lambda a: int(a[0]), input))
right = list(map(lambda a: int(a[1]), input))

total = 0
for i in range(0, len(left)):
    count = 0
    for y in range(0, len(right)):
        if left[i] == right[y]:
            count += 1
    total += left[i] * count

print('part2: ', total)

    