from utils.utils import file_get_contents

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

stepsDone = []
output = ""
while len(stepsToDo) > 0:
    for step in stepsToDo:
        reqsForStep = requirements[step]
        hasAllRequirements = True
        for req in reqsForStep:
            if req not in stepsDone:
                hasAllRequirements = False
                break

        if hasAllRequirements:
            stepsDone.append(step)
            stepsToDo.remove(step)
            output += step
            break

print("output for part 1: " + str(output))