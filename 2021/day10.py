with open('day10.txt') as f:
    lines = f.readlines()
    lines = list(map(lambda a: a.strip(), lines))

operators = [
    '()',
    '[]',
    '{}',
    '<>'
]

def is_start_operator(character):
    for i in range(len(operators)):
        if operators[i][0] == character:
            return True

    return False


def is_correct_end_operator(last_stack_operator, check_operator):
    return (last_stack_operator+check_operator) in operators

illigal_characters = []
valid_lines = []
for line in lines:
    size_changed = True
    stack = []
    valid = True

    for character in line:
        if is_start_operator(character):
            stack.append(character)
        else:
            if len(stack) == 0:
                # Need to implement this if it occures
                raise 'end character before start character'
            last_character = stack[-1]
            if is_correct_end_operator(last_character, character):
                stack.pop()
            else:
                illigal_characters.append(character)
                valid = False
                break
    if valid:
        valid_lines.append(stack)

price_lookup = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

c1 = 0
for character in illigal_characters:
    c1 += price_lookup[character]

print('part1: ', c1)

price_lookup2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

# autocomplete (part2)
scores2 = []
for line in valid_lines:
    to_add_characters = ''
    score = 0
    for character in reversed(line):
        for c in operators:
            if c[0] == character:
                to_add_characters += c[1]
                score *= 5
                score += price_lookup2[c[1]]
    scores2.append(score)

middle_score = sorted(scores2)[int(len(scores2)/2)]
print('part2: ', middle_score)

