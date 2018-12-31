from llist import dllist
import numpy as np

from utils.utils import file_get_contents


def getNext(list: dllist, iterable):
    if iterable.next:
        return iterable.next

    return list.first

def getPrev(list: dllist, iterable):
    if iterable.prev:
        return iterable.prev

    return list.last

file = file_get_contents('input.txt')
line = file.splitlines()[0]

lastMarble = int(line.split(' ')[6])
players = int(line.split(' ')[0])
scores = np.zeros(players)

round = 2
marbles = dllist([0, 1])
iterable = marbles.last
players = dllist(range(0,players))
playerIterable = players.first.next
while round <= (lastMarble * 100):
    if round % 23 == 0:
        for i in range(7):
            iterable = getPrev(marbles, iterable)

        newIterable = getNext(marbles, iterable)
        scores[playerIterable.value] += round + marbles.remove(iterable)
        iterable = newIterable
        #print(marbles)
        #print("curr pos", iterable)
        #print(iterable.next)
        #print(iterable.prev)
    else:
        iterable = getNext(marbles, iterable)
        iterable = getNext(marbles, iterable)
        if iterable == marbles.first:
            iterable = marbles.appendright(round)
        else:
            iterable = marbles.insert(round, iterable)
        #print(playerIterable)
        #print(marbles)
    round += 1
    playerIterable = getNext(players, playerIterable)

print("Part 1 result: " + str(int(np.max(scores))))