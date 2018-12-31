from utils.utils import file_get_contents

def shortenStr(pos: int, line: str):
    length = len(line)
    for id in range(length):
        idx = pos + id
        if idx + 1 == length:
            print("day one answer is: " + str(line))
            exit()
        toTest = line[idx] + line[idx + 1]
        if can_react(toTest):
            return [max(idx-1, 0), line[:idx] + line[idx+2:]]

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

pos = 0
while True:
    pos, line = shortenStr(pos, line)
    print(pos)
    print(len(line))


