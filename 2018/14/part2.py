from utils.utils import file_get_contents


def continueXTimesInArray(array, currentIndex, continueTimes):
    nextIndex = currentIndex
    for i in range(continueTimes):
        if nextIndex < len(array) - 1:
            nextIndex += 1
        else:
            nextIndex = 0

    return nextIndex


values = [3, 7]
elf1Index = 0
elf2Index = 1

file = file_get_contents('input.txt')
lines = file.splitlines()

outputExpected = []
for i in lines[0]:
    outputExpected.append(int(i))

outputExpectedLength = len(outputExpected)

while True:
    elf1Index = continueXTimesInArray(values, elf1Index, 1 + values[elf1Index])
    elf2Index = continueXTimesInArray(values, elf2Index, 1 + values[elf2Index])

    elf1Value = values[elf1Index]
    elf2Value = values[elf2Index]

    result = sum([elf1Value, elf2Value])
    if result >= 10:
        values.append(int(str(result)[0]))
        values.append(int(str(result)[1]))
    else:
        values.append(result)

    test = values[-outputExpectedLength:]
    if test == outputExpected:
        print("answer for part 2: " + str(len(values) - outputExpectedLength))
        exit()

    test2 = values[-(outputExpectedLength+1):-1]
    if test2 == outputExpected:
        print("Answer for part 2: " + str(len(values) - (outputExpectedLength+1)))
        exit()