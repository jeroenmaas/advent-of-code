import re

with open('day7.txt') as f:
    input = list(f.read().strip().split('\n'))

color_dict = {}
for line in input:
    r = re.match(r"(.*) bags contain", line)
    bag_color = r.group(1)
    line_without_bag = line.replace(r.group(), '').strip()
    color_dict[bag_color] = {}
    if "no other bags." not in line_without_bag:
        for bag in line_without_bag.split(', '):
            matchgroup2 = re.match(r"(\d*) (.*) bag", bag)
            color_dict[bag_color][matchgroup2.group(2)] = int(matchgroup2.group(1))

def get_bag_options(bag_color):
    output = {}
    for key, subbags in color_dict[bag_color].items():
        if key not in output:
            output[key] = 0
        output[key] += subbags
        for k, s2 in get_bag_options(key).items():
            if k not in output:
                output[k] = 0
            output[k] += s2 * subbags
    return output

def part1():
    c = 0
    for color in color_dict.keys():
        output = get_bag_options(color)
        if 'shiny gold' in output:
            c += 1
    return c

def part2():
    c = 0
    for item in get_bag_options('shiny gold').values():
        c += item
    return c

print('part1: ' + str(part1()))
print('part2: ' + str(part2()))
