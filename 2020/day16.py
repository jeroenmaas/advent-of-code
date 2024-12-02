import itertools
import json

from tqdm import tqdm

with open('day16.txt') as f:
    input_parts = f.read().strip().split('\n\n')

def parseValidationRule(txt):
    return {
        'name': txt.split(':')[0],
        'ranges': list(map(lambda a: list(map(lambda b: int(b), a.split('-'))), txt.split(': ')[1].split(' or ')))
    }

def is_rule_valid(rule, value):
    ranges = rule['ranges']
    for min, max in ranges:
        if value >= min and value <= max:
            return True

    return False

def is_rule_valid_for_list(rule, values):
    for v in values:
        if not is_rule_valid(rule, v):
            return False

    return True

def is_valid_order(order_option, possibilities_for_index):
    for i, o in enumerate(order_option):
        if o not in possibilities_for_index[i]:
            return False
    return True

validation_rules = list(map(lambda a: parseValidationRule(a), input_parts[0].split('\n')))
our_ticket = list(map(lambda a: int(a), input_parts[1].split('\n')[1].split(',')))
nearby_tickets = list(map(lambda a: list(map(lambda b: int(b), a.split(','))), input_parts[2].split('\n')[1:]))

invalid_values = []
valid_tickets = []
for t in nearby_tickets:
    is_valid_ticket = True
    for v in t:
        is_valid = False
        for rule in validation_rules:
            if is_rule_valid(rule, v):
               is_valid = True
               break
        if not is_valid:
           invalid_values.append(v)
           is_valid_ticket = False
    if is_valid_ticket:
        valid_tickets.append(t)

print('part1: ' + str(sum(invalid_values)))

values_by_index = []
for i in range(len(valid_tickets[0])):
    values_by_index.append([])

for t in valid_tickets:
    for i, v in enumerate(t):
        values_by_index[i].append(v)

possibilities_for_index = []
for i, values in enumerate(values_by_index):
    possibilities = []
    for rule in validation_rules:
        if is_rule_valid_for_list(rule, values):
            possibilities.append(rule['name'])
    possibilities_for_index.append(possibilities)

options = list(map(lambda a: [a], possibilities_for_index[0]))
for index, possibilities in enumerate(possibilities_for_index):
    if index == 0:
        continue

    options_to_check = itertools.product(options, possibilities)
    next_options = []
    for existing, new_option in options_to_check:
        if new_option not in existing:
            next_options.append(existing + [new_option])
    options = next_options

final_order = options[0]
values = []
for i, field in enumerate(final_order):
    if field.startswith('departure'):
        values.append(our_ticket[i])

output = 1
for v in values:
    output *= v

print('part2: ' + str(output))

