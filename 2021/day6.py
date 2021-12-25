def generate_empty_state():
    counted_state = {}
    for i in range(9):
        counted_state[i] = 0
    return counted_state

def run_iterations(counted_state, iters):
    for day in range(1, iters + 1):
        new_counted_state = generate_empty_state()
        for i in range(9):
            fish_count = counted_state[i]
            if i >= 1:
                new_counted_state[i - 1] += fish_count
            else:
                new_counted_state[6] += fish_count
                new_counted_state[8] = fish_count
        counted_state = new_counted_state

    c = 0
    for item in counted_state.values():
        c += item
    return c

with open('day6.txt') as f:
    state = list(map(lambda a: int(a), f.readline().split(',')))

counted_state = generate_empty_state()
for fish in state:
    counted_state[fish] += 1

print('part1: ', run_iterations(counted_state.copy(), 80))
print('part2: ', run_iterations(counted_state.copy(), 256))
