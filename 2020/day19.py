import json
import re
from random import choice

with open('day19.txt') as f:
    input = f.read().strip().split('\n\n')

def parse_lookups(text):
    return list(map(lambda a: int(a), text.split(' ')))

rules_input = input[0].split('\n')
to_test = input[1].split('\n')

rules = {}
for r in rules_input:
    rule_definition = r.split(': ')[1]

    if '|' in rule_definition:
        type = 'or'
        part1 = rule_definition.split(' | ')[0]
        part2 = rule_definition.split(' | ')[1]
        value = [parse_lookups(part1), parse_lookups(part2)]
    elif '"' in rule_definition:
        type = 'letter'
        value = rule_definition.replace('"', '')
    else:
        type = 'lookup'
        value = parse_lookups(rule_definition)

    rules[int(r.split(':')[0])] = {
        'type': type,
        'value': value
    }

def test_rule(rule, text):
    type = rule['type']
    value = rule['value']
    if type == 'letter':
        if len(text) == 0:
            return [False, ""]

        return [text[0] == value, text[1:]]
    elif type == 'lookup':
        text_left = text
        for i, v in enumerate(value):
            match, text_left = test_rule(rules[v], text_left)
            if not match:
                return [False, ""]
        return [True, text_left]
    elif type == 'or':
        matches = []
        for lookups in value:
            match, text_left = test_rule({'type': 'lookup', 'value': lookups}, text)
            if match:
                matches.append([match, text_left])

        if len(matches) == 0:
            return [False, ""]

        return choice(matches)
    else:
        print('unknown type')
        exit()

def find_matches(rules):
    match_ids = []
    for i, t in enumerate(json.loads(json.dumps(to_test))):
        match, left = test_rule(rules[0], t)
        if match and len(left) == 0:
            match_ids.append(i)
    return match_ids

print('part1: ' + str(len(find_matches(rules))))

rules[8] = {'type': 'or', 'value': [[42], [42, 8]]}
rules[11] = {'type': 'or', 'value': [[42, 31], [42, 11, 31]]}

# Why bother optimizing test_rule function with multiple input/outputs if we can just brute force our way
total_matches = set()
for i in range(100):
    total_matches.update(find_matches(rules))

print('part2: ' + str(len(total_matches)))

#
# print('part2: ' + str(len(find_matches(rules))))
# # total_matches.update(find_matches(rules))
