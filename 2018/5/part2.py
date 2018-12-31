from utils.utils import file_get_contents

def shortenStr(pos: int, line: str):
    length = len(line)
    for id in range(length):
        idx = pos + id
        if idx + 1 == length:
            return [None, line, True]
        toTest = line[idx] + line[idx + 1]
        if can_react(toTest):
            return [max(idx-1, 0), line[:idx] + line[idx+2:], False]

def can_react(toTest: str):
    if toTest.islower():
        return False

    if toTest.isupper():
        return False

    lower = toTest.lower()
    if lower[0] != lower[1]:
        return False

    return True

file = file_get_contents('input.txt')
line = file.splitlines()[0]

results = []
for char in "abcdefghijklmnopqrstuvwxyz":
    toTestStr = line.replace(char, "")
    toTestStr = toTestStr.replace(char.upper(), "")

    done = False
    pos = 0
    while not done:
        pos, toTestStr, done = shortenStr(pos, toTestStr)

    results.append([char, len(toTestStr)])

statsSorted = sorted(results, key=lambda r: r[1])

print("Answer to part 2 is " + str(statsSorted[0][1]))


