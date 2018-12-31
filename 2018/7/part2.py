import string

from utils.utils import file_get_contents

def getNextAvailableStep():
    for step in stepsToDo:
        reqsForStep = requirements[step]
        hasAllRequirements = True
        for req in reqsForStep:
            if req not in stepsDone:
                hasAllRequirements = False
                break

        if hasAllRequirements:
            stepsToDo.remove(step)
            return step

    return None

def processWork(worker, second):
    if worker["workingOn"] and worker["workingUtil"] <= second:
        stepsDone.append(worker["workingOn"])
        worker["workingOn"] = None
        worker["workingUtil"] = None


file = file_get_contents('input.txt')
lines = file.splitlines()

requirements = {}
for line in lines:
    stepToDo = line.split(' ')[1]
    ThenCanBegin = line.split(' ')[7]

    if stepToDo not in requirements:
        requirements[stepToDo] = []

    if ThenCanBegin not in requirements:
        requirements[ThenCanBegin] = []

    requirements[ThenCanBegin].append(stepToDo)

stepsToDo = sorted(requirements)
stepCount = len(stepsToDo)

stepsDone = []
output = ""
currentAmountOfSeconds = 0
workers = []
for _ in range(5):
    workers.append({"workingOn": None, "workingUtil": None})

while len(stepsDone) != stepCount:
    for worker in workers:
        processWork(worker, currentAmountOfSeconds)
        if worker["workingOn"]:
            continue

        newTask = getNextAvailableStep()
        if newTask:
            worker["workingOn"] = newTask
            worker["workingUtil"] = currentAmountOfSeconds + string.ascii_uppercase.index(newTask) + 61
    currentAmountOfSeconds += 1

print("output for part 2: " + str(currentAmountOfSeconds-1))