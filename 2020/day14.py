import math
import re
import time

with open('day14.txt') as f:
    input = f.read().strip().split('\n')

def convert_value_to_mask(value):
    output = ""
    for i in reversed(range(36)):
        bitvalue = pow(2, i)
        if value & bitvalue == bitvalue:
            output += '1'
        else:
            output += '0'
    return output

regex = r"mem\[(\d*)] = (\d*)"
input_parsed = []
current_mask = None
for line in input:
    if 'mask' in line:
        current_mask = {
            'mask': line.replace('mask = ', ''),
            'operations': []
        }
        input_parsed.append(current_mask)
    else:
        m = re.match(regex, line, re.M | re.I)
        memory_index = m.group(1)
        value = m.group(2)
        current_mask['operations'].append({
            'memory_index': int(memory_index),
            'value': int(value),
            'value_mask': convert_value_to_mask(int(value))
        })

def apply_mask(value_mask, mask):
    value_mask_list = list(value_mask)
    for i, v in enumerate(mask):
        if v == 'X':
            continue
        value_mask_list[i] = v
    return ''.join(value_mask_list)

def generate_mask_outcomes_part2(value_mask, mask):
    options = [list(value_mask)]
    for i, v in enumerate(mask):
        if v == 'X':
            new_options = []
            for o in options:
                o[i] = '0'
                copy = o.copy()
                copy[i] = '1'
                new_options.append(copy)
            options.extend(new_options)
        elif v == '1':
            for o in options:
                o[i] = '1'

    return map(lambda a: convert_mask_to_value(''.join(a)), options)

def convert_mask_to_value(value_mask):
    return int(value_mask, 2)

def part1():
    memory = {}
    for mask_info in input_parsed:
        mask = mask_info['mask']
        for op in mask_info['operations']:
            memory[op['memory_index']] = apply_mask(op['value_mask'], mask)

    return sum(map(lambda a: convert_mask_to_value(a), memory.values()))

def part2():
    memory = {}
    for mask_info in input_parsed:
        mask = mask_info['mask']
        for op in mask_info['operations']:
            memory_addresses = generate_mask_outcomes_part2(convert_value_to_mask(op['memory_index']), mask)
            for m in memory_addresses:
                memory[m] = op['value']

    return sum(memory.values())

print('part1: ' + str(part1()))
print('part2: ' + str(part2()))
