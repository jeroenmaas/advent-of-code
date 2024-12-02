import math
import re

with open('day4.txt') as f:
    input = map(lambda a: a.replace('\n', ' '), f.read().split('\n\n'))

def is_valid_passport_part2(p):
    if len(p.keys()) != 8:
        return False

    for elem in ['iyr', 'hgt', 'hcl', 'ecl', 'byr', 'eyr', 'pid', 'cid']:
        if elem not in p.keys():
            return False

    if len(p['byr']) != 4 or (int(p['byr']) >= 1920 and int(p['byr']) <= 2002) == False:
        return False

    if len(p['iyr']) != 4 or (int(p['iyr']) >= 2010 and int(p['iyr']) <= 2020) == False:
        return False

    if len(p['eyr']) != 4 or (int(p['eyr']) >= 2020 and int(p['eyr']) <= 2030) == False:
        return False

    regex = r"(\d*)(\S*)"
    m = re.match(regex, p['hgt'], re.M|re.I)
    length = m.group(1)
    type = m.group(2)
    if type not in ['cm', 'in']:
        return False
    elif type == 'cm' and not (int(length) >= 150 and int(length) <= 193):
        return False
    elif type == 'in' and not (int(length) >= 59 and int(length) <= 76):
        return False
    elif m.group(0) != p['hgt']:
        print(p['hgt'])
        return False

    regex = r"#[0-9a-f]{6}"
    m = re.match(regex, p['hcl'], re.M | re.I)
    if not m or len(p['hcl']) != 7:
        return False

    if len(p['ecl']) != 3 or p['ecl'] not in 'amb blu brn gry grn hzl oth'.split(' '):
        return False

    regex = r"[0-9]{9}"
    m = re.match(regex, p['pid'], re.M | re.I)
    if not m or len(p['pid']) != 9:
        return False

    return True

c1 = 0
c2 = 0
for passport in input:
    passportParts = passport.split(' ')
    elements = {}
    for p in passportParts:
        if ":" not in p:
            continue

        index = p.split(':')[0]
        value = p.split(':')[1]
        elements[index] = value

    elements['cid'] = 'not_important'

    if len(elements.keys()) == 8:
        c1 += 1

    if is_valid_passport_part2(elements):
        c2 += 1

print('part1: ' + str(c1))
print('part2: ' + str(c2))

#122 to high
