"""
idea:

1) fuer den 1. Wuerfel alle moeglichen Permutationen generieren
2) Durchgehen, falls Permutation unmoeglich zum Ergebnis fueren kann ueberspringen, sonst 3)
3) Fuer Wuerfel 2 schauen was aufgrund der Belegung von Wuerfel 1 definitiv enthalten sein muss
   6 - diese Zahl * (moegliche weitere Zahlen) ist die Anzahl der Kombinationen wenn Wuerfel 1 diese Belegung hat

"""
import time

import itertools


def main():
    sides = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # generate all valid combinations for the first dice (including adding 6 if there's a 9 and visa versa
    tmp_combinations = list(itertools.combinations(sides, 6))
    combinations = []
    for tmp_combination in tmp_combinations:
        combination = set()
        for side in tmp_combination:
            combination.add(side)
            if side == 6:
                combination.add(9)
            elif side == 9:
                combination.add(6)
        combinations.append(combination)

    print(combinations)
    print('is possible:', generates_all_squares({0, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 8, 9}))

    count = 0
    for i in range(len(combinations)):
        dice1 = combinations[i]
        for j in range(i+1, len(combinations)):
            dice2 = combinations[j]
            if generates_all_squares(dice1, dice2):
                count += 1

    print('count of distinct cube digit pairs:', count)


def generates_all_squares(dice1, dice2):
    squares = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1)]
    for i, j in squares:
        if not ((i in dice1 and j in dice2) or (j in dice1 and i in dice2)):
            return False
    return True


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)