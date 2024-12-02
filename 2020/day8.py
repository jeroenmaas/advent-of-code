import copy
import re

def read_instruction(instruction):
    b = instruction.split(' ')
    b[1] = int(b[1])
    return b

with open('day8.txt') as f:
    input = list(map(lambda a: read_instruction(a), f.read().strip().split('\n')))


def run_program(input):
    offset = 0
    passed_instructions = []
    g = 0
    exitcode = None
    while(True):
        if offset in passed_instructions:
            exitcode = 'invalid'
            break

        if offset >= len(input):
            exitcode = None
            break

        passed_instructions.append(offset)
        operation = input[offset][0]
        argument = input[offset][1]
        if operation == 'nop':
            offset += 1
        elif operation == 'jmp':
            offset += argument
        elif operation == 'acc':
            g += argument
            offset += 1
        else:
            exit('unknown instruction')

    return {"exitcode": exitcode, "g": g}

# 542 to low
def part1():
    return run_program(input)['g']

def part2():
    for offset, element in enumerate(input):
        if element[0] == 'jmp':
            test_input = copy.deepcopy(input)
            instruction = copy.deepcopy(element)
            instruction[0] = 'nop'
            test_input[offset] = instruction
        elif element[0] == 'nop':
            test_input = copy.deepcopy(input)
            instruction = copy.deepcopy(element)
            instruction[0] = 'jmp'
            test_input[offset] = instruction
        else:
            continue

        result = run_program(test_input)
        if result['exitcode'] == None:
            return result['g']

print('part1: ' + str(part1()))
print('part2: ' + str(part2()))
