import re

with open('day18.txt') as f:
    input = f.read().strip().split('\n')

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def execute(text):
    parts = text.split(' ')
    output = int(parts.pop(0))
    for operator, value in chunks(parts, 2):
        if operator == '*':
            output *= int(value)
        elif operator == '+':
            output += int(value)
    return output

def execute2(line):
    regex = r"\d+ \+ \d+"
    while(True):
        m = re.search(regex, line, re.MULTILINE)
        if not m:
            break
        first_piece = line[:m.start()]
        third_piece = line[m.end():]
        line = first_piece + str(execute(m.group(0))) + third_piece

    return execute(line)

def calculate(execution_function):
    regex = r"\([^()]+\){1}"
    results = []
    for line in input:
        while(True):
            m = re.search(regex, line, re.MULTILINE)
            if not m:
                break
            first_piece = line[:m.start()]
            third_piece = line[m.end():]
            line = first_piece + str(execution_function(m.group(0).replace('(', '').replace(')', ''))) + third_piece

        results.append(execution_function(line))
    return results

print('part1: ' + str(sum(calculate(execute))))
print('part2: ' + str(sum(calculate(execute2))))
