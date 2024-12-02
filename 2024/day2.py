with open('day2.txt') as f:
    input = f.readlines()
    input = list(map(lambda a: list(map(lambda b: int(b), a.strip().split(' '))), input))
    
#print(input)

safe = 0
for i in range(0, len(input)):
    r = input[i]

    if r == sorted(r) or r == sorted(r, reverse=True):
        
        success = True
        for y in range(1, len(r)):
            left = r[y-1]
            right = r[y]
            if abs(left - right) > 0 and abs(left - right) < 4:
               continue
            else:
                success = False
                break
        
        if success:
            safe += 1

print('part1: ', safe)

def checkRange(r):
    if r == sorted(r) or r == sorted(r, reverse=True):
        
        success = True
        for y in range(1, len(r)):
            left = r[y-1]
            right = r[y]
            if abs(left - right) > 0 and abs(left - right) < 4:
               continue
            else:
                success = False
                break
        
        if success:
            return True
    
    return False

safe = 0
for i in range(0, len(input)):
    r = input[i]

    if checkRange(r):
        safe += 1
        continue

    for i in range(0, len(r)):
        r2 = r.copy()
        r2.pop(i)

        if checkRange(r2):
            safe += 1
            break


print('part2: ', safe)
                