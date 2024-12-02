with open('day1.txt') as f:
    input = f.readlines()
    input = list(map(lambda a: a.strip(), input))

outputs = []
for line in input:

    replaces = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    digit_options = [str(v) for v in replaces.values()] + [k for k in replaces.keys()]

    first_options = {}
    last_options = {}

    for option in digit_options:
        o = line.find(option)
        if o != -1:
            first_options[option] = o

        o = line.rfind(option)
        if o != -1:
            last_options[option] = o

    first = min(first_options, key=first_options.get)
    last = max(last_options, key=last_options.get)

    first_value = str(first if first.isdigit() else replaces[first])
    last_value = str(last if last.isdigit() else replaces[last])

    outputs.append(int(first_value + last_value))

print(sum(outputs))