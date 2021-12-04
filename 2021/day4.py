import copy


def calculate_part1(board, drawn_digits):
    last_drawn = drawn_digits[-1]

    value = 0
    for line in board:
        for digit in line:
            if digit not in drawn_digits:
                value += digit

    return value * last_drawn

with open('day4.txt') as f:
    input = f.readlines()

drawable_numbers = list(map(lambda a: int(a), input[0].split(',')))

boards = []
tmp_board = []
for line in input[2:]:
    if len(line) == 1:
        boards.append(tmp_board)
        tmp_board = []
        continue

    tmp_board.append(list(map(lambda a: int(a), line.strip().replace('  ', ' ').split(' '))))
if len(tmp_board) > 0:
    boards.append(tmp_board)

all_boards = copy.deepcopy(boards)
board_length = 5
drawn_numbers = []
first = True
last_score = 0
for n in drawable_numbers:
    drawn_numbers.append(n)
    # check if we have a winner
    for board in boards:
        winner = False

        for line in board:
            if set(line).issubset(set(drawn_numbers)):
               if first:
                   print('part1: ', calculate_part1(board, drawn_numbers))
                   first = False
               winner = True
               last_score = calculate_part1(board, drawn_numbers)
               boards.remove(board)
               break

        if winner:
            continue

        for y in range(board_length):
            items = [board[0][y], board[1][y], board[2][y], board[3][y], board[4][y]]
            if set(items).issubset(set(drawn_numbers)):
                if first:
                    print('part1: ', calculate_part1(board, drawn_numbers))
                    first = False
                winner = True
                last_score = calculate_part1(board, drawn_numbers)
                boards.remove(board)
                break

print('part2: ', last_score)


