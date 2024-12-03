with open('day3.txt') as f:
    input = f.readlines()

v = 0
for i in range(0, len(input)):
    r = input[i]

    import re

    regex = r"mul\((\d+),(\d+)\)"
    matches = re.finditer(regex, r, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):        
        val1 = match.group(1)
        val2 = match.group(2)

        v += int(val1) * int(val2)

print('part1: ', v)

import re


totalValue = 0
totalLine = ""
for i in range(0, len(input)):
    totalLine += input[i]

regex_dont = r"don't\(\)"
matches = re.finditer(regex_dont, totalLine, re.MULTILINE)
commands = []
for matchNum, match in enumerate(matches, start=1):
    commands.append([match.start(), False])

dos = []
regex_do = r"do\(\)"
matches = re.finditer(regex_do, totalLine, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    commands.append([match.start(), True])

commands = sorted(commands, key=lambda x: x[0])

regex = r"mul\((\d+),(\d+)\)"
matches = re.finditer(regex, totalLine, re.MULTILINE)


for matchNum, match in enumerate(matches, start=1):        
    val1 = match.group(1)
    val2 = match.group(2)

    previousCommand = True
    finalCommand = None
    for i in range(0, len(commands)):
        if commands[i][0] < match.start():
            previousCommand = commands[i][1]
            finalCommand = commands[i]

    if previousCommand:
        totalValue += int(val1) * int(val2)

print('part2: ', totalValue)
