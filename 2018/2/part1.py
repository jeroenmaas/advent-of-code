from utils.utils import file_get_contents

file = file_get_contents('input.txt')

twoLetterCounts = 0
threeLetterCounts = 0

for line in file.splitlines():
    setLine = set(line)
    hasTwo = False
    hasThree = False

    for item in setLine:
        count = line.count(item)
        if count == 2:
            hasTwo = True
        if count == 3:
            hasThree = True

    if hasTwo:
        twoLetterCounts += 1
    if hasThree:
        threeLetterCounts += 1

print(twoLetterCounts)
print(threeLetterCounts)
print("First part: " + str(twoLetterCounts*threeLetterCounts))

