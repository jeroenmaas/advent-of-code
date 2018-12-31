from utils.utils import file_get_contents
import numpy as np


def convertToBooleanNP(plants: str, padding=0):
    result = np.zeros(len(plants) + padding * 2)
    for idx, char in enumerate(plants):
        result[idx + padding] = char == "#"
    return result


def actionExists(action, actions):
    for testAction in actions:
        if (testAction == action).all():
            return True
    return False


file = file_get_contents('input.txt')
initStr = file.splitlines()[0].split('initial state: ')[1]

actions = []
actionLines = file.splitlines()[2:]
for line in actionLines:
    parts = line.split(' => ')
    if parts[1] == "#":
        actions.append(convertToBooleanNP(parts[0]))

actions = np.asarray(actions)

iterations = 20
plantState = convertToBooleanNP(initStr, iterations * 2)

print(plantState)
for i in range(iterations):
    newPlantState = plantState.copy()
    for y in range(len(plantState) - 4):
        toCheck = plantState[y:y + 5]

        print(toCheck)

        if actionExists(toCheck, actions):
            newPlantState[y + 2] = 1
        else:
            newPlantState[y + 2] = 0
    plantState = newPlantState

indexesWithPlants = np.transpose((plantState>0).nonzero())
accountForPadding = iterations*len(indexesWithPlants)*2
sumOfIndexes = indexesWithPlants.sum()

print("Answer for part 1 = ", str(sumOfIndexes - accountForPadding))