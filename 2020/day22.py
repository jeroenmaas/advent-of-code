import json
from random import randint

with open('day22.txt') as f:
    inputs = f.read().strip().split('\n\n')

def part1():
    player1_dek = list(map(lambda a: int(a), inputs[0].split('\n')[1:]))
    player2_dek = list(map(lambda a: int(a), inputs[1].split('\n')[1:]))
    while(len(player1_dek) > 0 and len(player2_dek) > 0):
        player1_card = player1_dek.pop(0)
        player2_card = player2_dek.pop(0)

        if player1_card > player2_card:
            player1_dek.extend([player1_card, player2_card])
        else:
            player2_dek.extend([player2_card, player1_card])

    dek = player1_dek if len(player2_dek) == 0 else player2_dek
    output = 0
    for i, v in enumerate(reversed(dek)):
        output += v * (i+1)

    return output

game_cache = {}
iterationsCount = {'c': 0}

def generate_game_hash(dek1, dek2):
    return hash(','.join(map(lambda a: str(a), dek1)) + '_' + ','.join(map(lambda a: str(a), dek2)))

def play(player1_dek, player2_dek, game):
    round = 1
    previous_rounds = []
    while (len(player1_dek) > 0 and len(player2_dek) > 0):
        game_hash = generate_game_hash(player1_dek, player2_dek)
        if game_hash in previous_rounds:
            game_cache[game_hash] = {
                'winner': 1,
                'player1_dek': player1_dek,
                'player2_dek': player2_dek
            }
            return game_cache[game_hash]

        previous_rounds.append(game_hash)
        player1_card = player1_dek.pop(0)
        player2_card = player2_dek.pop(0)


        if len(player1_dek) >= player1_card and len(player2_dek) >= player2_card:
            game_hash = generate_game_hash(player1_dek[:player1_card], player2_dek[:player2_card])
            if game_hash in game_cache:
               outcome = game_cache[game_hash]
            else:
                outcome = play(json.loads(json.dumps(player1_dek[:player1_card])), json.loads(json.dumps(player2_dek[:player2_card])), game+1)
                game_cache[game_hash] = outcome

            if outcome['winner'] == 1:
                player1_dek.extend([player1_card, player2_card])
            else:
                player2_dek.extend([player2_card, player1_card])
        else:
            if player1_card > player2_card:
                player1_dek.extend([player1_card, player2_card])
            else:
                player2_dek.extend([player2_card, player1_card])

        iterationsCount['c'] += 1


    return {
        'winner': 1 if len(player1_dek) > 0 else 2,
        'player1_dek': player1_dek,
        'player2_dek': player2_dek
    }

def part2():
    player1_dek = list(map(lambda a: int(a), inputs[0].split('\n')[1:]))
    player2_dek = list(map(lambda a: int(a), inputs[1].split('\n')[1:]))

    game = 1
    result = play(player1_dek, player2_dek, game)
    player1_dek = result['player1_dek']
    player2_dek = result['player2_dek']

    dek = player1_dek if len(player2_dek) == 0 else player2_dek
    output = 0
    for i, v in enumerate(reversed(dek)):
        output += v * (i+1)

    return output

print('part1: ', part1())
print('part2: ', part2())
