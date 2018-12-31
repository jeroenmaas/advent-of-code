from datetime import datetime
from datetime import timedelta

from utils.utils import file_get_contents
import numpy as np
import re

file = file_get_contents('input.txt')
lines = file.splitlines()
lines.sort()

firstDate = None

actionsByDay = {}

guards = {}
for line in lines:
    print(line)
    date = re.search('\[(.*?)\]', line).group(1)
    action = line.split(']')[1][1:]
    parsedDate = datetime.strptime(date, '%Y-%m-%d %H:%M')
    if parsedDate.hour > 20:
        parsedDate += timedelta(days=1)
        parsedDate = parsedDate

    if firstDate is None:
        firstDate = parsedDate

    delta = parsedDate - firstDate
    if not delta.days in actionsByDay:
        actionsByDay[delta.days] = []

    actionsByDay[delta.days].append([parsedDate, action])

x = np.zeros((len(actionsByDay),60))
for idx, actionInfos in actionsByDay.items():
    sleepStart = None
    for actionInfo in actionInfos:
        date = actionInfo[0] # type: datetime
        action = actionInfo[1]

        if "Guard" in action:
            guardId = re.search('#(.*?) ', action).group(1)
            guards[idx] = guardId
        if "falls asleep" in action:
            sleepStart = date.minute
        if "wakes up" in action:
            for i in range(date.minute - sleepStart):
                x[idx, sleepStart+i] = 1
            sleepStart = 0

statsPerGuard = {}


for idx, line in enumerate(x):
    guardId = int(guards[idx])
    if not guardId in statsPerGuard:
        statsPerGuard[guardId] = {"sleepMinutes": 0, "count": 0, "dayIndexes": []}

    statsPerGuard[guardId]["sleepMinutes"] += len(np.argwhere(line == 1))
    statsPerGuard[guardId]["count"] += 1
    statsPerGuard[guardId]["dayIndexes"].append(idx)
    statsPerGuard[guardId]["guardId"] = guardId

for guardId, stat in statsPerGuard.items():
    sumMinutes = np.zeros((60,))
    for index in stat["dayIndexes"]:
        sumMinutes += x[index]

    stat["maxAsleepOnMinute"] = np.argmax(sumMinutes)
    stat["AmountOfSleeps"] = np.max(sumMinutes)

# print(statsPerGuard)
# print(list(statsPerGuard.values()))

statsSorted = sorted(statsPerGuard.values(), key=lambda g: g["AmountOfSleeps"], reverse=True)

guardStatsWithMostSleepMinutesPerWatch = statsSorted[0]

print(guardStatsWithMostSleepMinutesPerWatch)
answer = guardStatsWithMostSleepMinutesPerWatch["maxAsleepOnMinute"] * guardStatsWithMostSleepMinutesPerWatch["guardId"]
print("Enter this for day 2: " + str( answer))

np.set_printoptions(threshold=np.nan)
#print(x)




