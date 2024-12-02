with open('day4.txt') as f:
    input = f.readlines()

cards = []
for line in input:
    cards.append({
        'id': line[5:].split(':')[0],
        'winning': list(map(lambda a: int(a.strip()), line.split(':')[1].strip().split('|')[0].strip().replace('  ', ' 0').split(' '))),
        'draw': list(map(lambda a: int(a.strip()), line.split(':')[1].strip().split('|')[1].strip().replace('  ', ' 0').split(' '))),
    })

points = 0
for c in cards:
    f = 0
    for d in c['draw']:
        if d in c['winning']:
            f += 1

    if f > 0:
        points += pow(2, f-1)

print('part1: ', points)

points = 0
drawsByCard = [1 for c in cards]
for index, c in enumerate(cards):
    multiplier = drawsByCard[index]

    f = 0
    for d in c['draw']:
        if d in c['winning']:
            f += 1

    for i in range(f):
        newIndex = index + i + 1
        if newIndex >= len(cards):
            break
        drawsByCard[newIndex] += multiplier

print('part2: ', sum(drawsByCard))



