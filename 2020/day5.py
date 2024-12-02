with open('day5.txt') as f:
    input = list(map(lambda a: [a.strip()[:7], a.strip()[7:]], f.readlines()))

seat_ids = []
for s in input:
    row = int(s[0].replace('B', '1').replace('F', '0'), 2)
    column = int(s[1].replace('R', '1').replace('L', '0'), 2)
    seat_ids.append(row * 8 + column)

print('part1: ' + str(max(seat_ids)))

seat_ids.sort()
last = None
for i in seat_ids:
    if last != None and i != last+1:
        print('part2: ' + str(i-1))
        exit()
    last = i
