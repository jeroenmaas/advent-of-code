with open('day7.txt') as f:
    positions = list(map(lambda a: int(a), f.readline().split(',')))

cost_by_position_part1 = {}
cost_by_position_part2 = {}
for new_position in range(1000):
    print(new_position)

    cost1 = 0
    cost2 = 0
    for item in positions:
        for i in range(abs(item - new_position)):
            cost2 += 1 + i
        cost1 += abs(item - new_position)

    cost_by_position_part1[new_position] = cost1
    cost_by_position_part2[new_position] = cost2

cheapest_option1 = min(cost_by_position_part1.items(), key=lambda x: x[1])
cheapest_option2 = min(cost_by_position_part2.items(), key=lambda x: x[1])

print('part1: ', cheapest_option1[1])
print('part2: ', cheapest_option2[1])