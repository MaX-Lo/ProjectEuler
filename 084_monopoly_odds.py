"""
idea:
"""
import copy
import random
import time


def main():
    repeat = 100

    board = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',  # 1
             'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',  # 2
             'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',  # 3
             'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']  # 4

    probabilities = {field: 0 for field in board}
    for i in range(repeat):
        res = play()
        for field in res:
            probabilities[field] += res[field]

        best_of(probabilities)


def best_of(dictionary: dict):
    d = copy.deepcopy(dictionary)

    best = find_key(max(d.values()), d)
    print(best, d[best])
    d[best] = 0
    best = find_key(max(d.values()), d)
    print(best, d[best])
    d[best] = 0
    best = find_key(max(d.values()), d)
    print(best, d[best])


def find_key(value, d):
    for key in d:
        if value == d[key]:
            return key


def play():
    # String coding for every field
    #         1       2     3      4      5     6     7      8      9     10
    board = ['GO',   'A1', 'CC1', 'A2',  'T1', 'R1', 'B1',  'CH1', 'B2', 'B3',  # 1
             'JAIL', 'C1', 'U1',  'C2',  'C3', 'R2', 'D1',  'CC2', 'D2', 'D3',  # 2
             'FP',   'E1', 'CH2', 'E2',  'E3', 'R3', 'F1',  'F2',  'U2', 'F3',  # 3
             'G2J',  'G1', 'G2',  'CC3', 'G3', 'R4', 'CH3', 'H1',  'T2', 'H2']  # 4

    # keeps track of the number of visits for each field
    visit = {field: 0 for field in board}

    # defines for every field it's integer position on the board, so that it's easier
    # to determine which fields are behind ore ahead of a given field
    str_pos_to_int_pos = {board[i]: i for i in range(len(board))}

    community_chest = ['GO', 'JAIL']
    community_chest.extend(['NONE' for _ in range(14)])
    community_chest = shuffle(community_chest)

    chance = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'next_r', 'next_r', 'next_u', 'back_3']
    chance.extend(['NONE' for _ in range(6)])
    chance = shuffle(chance)

    # ToDo shuffle community chest and chance cards

    start_position = 'GO'
    position = start_position

    count = 0
    for turn in range(1, 1000000):
        # if count % 500000 == 0:
        #     if count == 0:
        #         count = 1
        #     print(count, [(x, round(visit[x]/count*100, 3)) for x in ['JAIL', 'E3', 'GO']])

        for roll in range(1, 4):
            dice1, dice2 = roll_dices(4)
            count += 1

            if dice1 == dice2 and roll == 3:
                position = 'JAIL'
                visit[position] += 1
                break

            position = board[(str_pos_to_int_pos[position] + dice1 + dice2) % 40]

            position, can_continue = evaluate_roll(position, board, str_pos_to_int_pos,
                                                   community_chest, chance)
            visit[position] += 1
            if not can_continue:
                break

            if dice1 != dice2:
                break

    res = {x: (visit[x] / count * 100) for x in board}
    return res


def evaluate_roll(position, board, str_pos_to_int_pos, community_chest, chance):

    if position == 'G2J':
        return 'JAIL', False

    if position in ['CC1', 'CC2', 'CC3']:
        cc_card = community_chest.pop(0)
        community_chest.append(cc_card)

        if cc_card == 'GO':
            return 'GO', True
        elif cc_card == 'JAIL':
            return 'JAIL', False

    elif position in ['CH1', 'CH2', 'CH3']:
        c_card = chance.pop(0)
        chance.append(c_card)

        if c_card == 'JAIL':
            return 'JAIL', False
        elif c_card == 'next_r':
            return get_next_railway(str_pos_to_int_pos[position]), True
        elif c_card == 'next_u':
            return get_next_utility_company(str_pos_to_int_pos[position]), True
        elif c_card == 'back_3':
            position = board[(str_pos_to_int_pos[position] - 3) % 40]
            return evaluate_roll(position, board, str_pos_to_int_pos, community_chest, chance)
        elif not (c_card == 'NONE'):
            return c_card, True

    return position, True


def roll_dices(sides):
    dice1 = random.randint(1, sides)
    dice2 = random.randint(1, sides)
    return dice1, dice2


def shuffle(l):
    """ take a list and return a new list with it's elements in a random order """
    new_l = []
    for i in range(len(l)-1, 0, -1):
        r = random.randint(0, i)
        new_l.append(l.pop(r))
    new_l.append(l[0])
    return new_l


def get_next_railway(pos):
    if 35 <= pos or pos <= 4:
        return 'R1'
    elif 5 <= pos <= 14:
        return 'R2'
    elif 15 <= pos <= 24:
        return 'R3'
    elif 25 <= pos <= 34:
        return 'R4'
    else:
        print('error get next railway')


def get_next_utility_company(pos):
    if 28 <= pos or pos <= 11:
        return 'U1'
    elif 12 <= pos <= 27:
        return 'U2'
    else:
        print('error get next utility company')


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)