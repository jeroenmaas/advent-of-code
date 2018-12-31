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

amountOfRecipies = int(lines[0])
amountOfScoresAfterRecipiesCheck = 10

for i in range(amountOfRecipies + amountOfScoresAfterRecipiesCheck):
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

    if len(values) >= amountOfRecipies+amountOfScoresAfterRecipiesCheck:
        output = ""
        result = values[amountOfRecipies:amountOfRecipies+amountOfScoresAfterRecipiesCheck]
        for i in result:
            output += str(i)

        print("Day 1 result is: " + output)
        exit()