import numpy

with open('day2.txt') as f:
    input = f.readlines()

data = []
for line in input:
    gameId = line[5:].split(':')[0]
    line = line.split(':')[1]
    listOfCubes = []
    for parts in line.split(';'):
        cubes = parts.strip().split(',')
        for c in cubes:
            count = c.strip().split(' ')[0]
            color = c.strip().split(' ')[1]
            listOfCubes.append({
                'count': count,
                'color': color
            })
    data.append({
        'gameId': gameId,
        'cubes': listOfCubes
    })

def part1():
    allowed_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    allowed_games = []
    for game in data:
        cubes = game['cubes']
        err = False
        for cube in cubes:
            if cube['color'] not in allowed_cubes:
                raise Exception('Invalid color: ' + cube['color'])

            allowed_cube_count = allowed_cubes[cube['color']]
            if allowed_cube_count < int(cube['count']):
                err = True
                break

        if not err:
            allowed_games.append(game)

    print('part1: ', sum([int(game['gameId']) for game in allowed_games]))


def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result
def part2():
    sums = []
    for game in data:
        m = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        cubes = game['cubes']
        for c in cubes:
            if c['color'] not in m:
                raise Exception('Invalid color: ' + c['color'])
            if m[c['color']] < int(c['count']):
                m[c['color']] = int(c['count'])
        sums.append(multiplyList(m.values()))

    print('part2: ', sum(sums))

part1()
part2()