with open('day2.txt') as f:
    input = f.readlines()


count_valid_part1 = 0
count_valid_part2 = 0
for item in input:
    rule, output = item.split(': ')
    min_max, character = rule.split(' ')
    min, max = min_max.split('-')

    character_count = 0
    for i in output:
        if i == character:
            character_count += 1

    if character_count >= int(min) and character_count <= int(max):
        count_valid_part1 += 1

    character_at_first_index = output[int(min)-1]
    character_at_second_index = output[int(max)-1]

    if character_at_first_index == character and character_at_second_index != character:
        count_valid_part2 += 1
    elif character_at_first_index != character and character_at_second_index == character:
        count_valid_part2 += 1

print('part2: ' + str(count_valid_part2))
