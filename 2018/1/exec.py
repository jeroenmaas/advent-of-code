from utils.utils import file_get_contents

file = file_get_contents('input.txt')

totalInterval = 0
existingIntervals = set()

for i in range(1000):
    for line in file.splitlines():
        value = line[1:]
        if line[0] == "+":
            totalInterval += int(value)
        else:
            totalInterval -= int(value)

        if totalInterval in existingIntervals:
            print(totalInterval)
            print("we are done")
            exit()

        existingIntervals.update([totalInterval])

    print("Day 1 step 1 answer: " + str(totalInterval))

print("Did not found the answer after 1000 intervals")