with open('day1.txt') as f:
    input = f.readlines()
    input = list(map(lambda a: a.strip(), input))

outputs = []
for line in input:

    replaces = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    # Part 2
    # for index in range(len(line)):
    #     for toReplace, replaceWith in replaces.items():
    #         if line[index:].startswith(toReplace):
    #             line = line.replace(toReplace, toReplace[0] + str(replaceWith) + toReplace[-1], 1)
    #             break

    digits = []
    for c in line:
        if c.isdigit():
            digits.append(c)
    outputs.append(int(digits[0] + digits[-1]))

print(sum(outputs))
