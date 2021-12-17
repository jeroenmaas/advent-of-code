with open('day17.txt') as f:
    input = f.readline()
print(input)

targetxmin = input.split('target area: x=')[1].split("..")[0]
targetxmax = input.split('target area: x=')[1].split("..")[1].split(',')[0]
targetx = [int(targetxmin), int(targetxmax)]

targetymin = input.split('y=')[1].split("..")[0]
targetymax = input.split('y=')[1].split("..")[1].split(',')[0]
targety = [int(targetymin), int(targetymax)]

highestxvelocity = targetx[1]

def get_max_x_position_for_velocity(x_velocity):
    distance = 0
    while x_velocity > 0:
        distance += x_velocity
        x_velocity -= 1

    return distance

test = 0
while get_max_x_position_for_velocity(test) < targetx[0]:
    test += 1
lowestxvelocity = test

lowestyvelocity = targety[0]

def check_velocity(velocity):
    origin_velocity = [velocity[0], velocity[1]]
    highest_y = 0
    position = [0, 0]
    while velocity[1] > 0 or position[1] > targety[0]:
        position[0] += velocity[0]
        position[1] += velocity[1]

        if position[1] > highest_y:
            highest_y = position[1]

        if velocity[0] != 0:
            positive = velocity[0] > 0
            velocity[0] = (abs(velocity[0]) - 1) * (1 if positive else -1)
        velocity[1] -= 1

        if position[0] >= targetx[0] and position[0] <= targetx[1]:
            if position[1] >= targety[0] and position[1] <= targety[1]:
                return origin_velocity, highest_y

    return None

velocities = []
for yspeed in reversed(range(lowestyvelocity, 300)):
    for xspeed in range(lowestxvelocity-1, highestxvelocity+1):
        result = check_velocity([xspeed, yspeed])
        if result:
            velocities.append(result)

print('part1: ', velocities[0][1])
print('part2: ', len(velocities))