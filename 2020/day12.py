import json
import math

with open('day12.txt') as f:
    commands = list(map(lambda s: [s[0], int(s[1:])], f.read().strip().split('\n')))

# N == 0, E == 1, S == 2, W == 3

def move(state, positions, direction):
    if direction == 0:
        state['y'] += positions
    elif direction == 1:
        state['x'] += positions
    elif direction == 2:
        state['y'] -= positions
    elif direction == 3:
        state['x'] -= positions
    else:
        raise 'invalid direction: ' + str(direction)
    return state

def rotate(state, degrees):
    dir = state['dir']
    dir += degrees / 90

    while(dir > 3):
        dir -= 4

    while(dir < 0):
        dir += 4

    state['dir'] = dir
    return state

current_state = {"dir": 1, "x": 0, "y": 0}
waypoint = {"x": 10, "y": 1}

def part1(current_state):
    for c in commands:
        action = c[0]
        value = c[1]

        if action == 'N':
            current_state = move(current_state, value, 0)
        elif action == 'S':
            current_state = move(current_state, value, 2)
        elif action == 'E':
            current_state = move(current_state, value, 1)
        elif action == 'W':
            current_state = move(current_state, value, 3)
        elif action == 'L':
            current_state = rotate(current_state, -value)
        elif action == 'R':
            current_state = rotate(current_state, value)
        elif action == 'F':
            current_state = move(current_state, value, current_state['dir'])

        print('part1: ' + str(abs(current_state['x']) + abs(current_state['y'])))

def rotate2(waypoint, value):
    r = rotate({"dir": 0}, value)['dir']

    angle = -r * (math.pi / 2)

    ox, oy = [0, 0]
    px, py = [waypoint['x'], waypoint['y']]

    qx = round(ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy))
    qy = round(oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy))

    waypoint['x'] = qx
    waypoint['y'] = qy
    return waypoint

def rotate3(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """

    return qx, qy

def part2(current_state, waypoint):
    for c in commands:
        action = c[0]
        value = c[1]

        if action == 'L':
            action = 'R'
            value = 360-value

        if action == 'N':
            waypoint['y'] += value
            #current_state = move(current_state, value, 0)
        elif action == 'S':
            waypoint['y'] -= value
        elif action == 'E':
            waypoint['x'] += value
        elif action == 'W':
            waypoint['x'] -= value
        elif action == 'R':
            waypoint = rotate2(waypoint, value)
        elif action == 'F':
            current_state['x'] += waypoint['x'] * value
            current_state['y'] += waypoint['y'] * value
        else:
            print('unknown action: ' + action)

    print('part2: ' + str(abs(current_state['x']) + abs(current_state['y'])))

part2(current_state, waypoint)

# 24769?

# 29277 to high
# 177429 to high
