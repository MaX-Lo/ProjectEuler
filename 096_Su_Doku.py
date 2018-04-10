"""
idea:
1) oben links mit 1 beginnend versuchen einzusetzen und Feld 0,0 in ein Set aufnehmen
2) zum naechsten Feld gehen (immer nach rechts, dann neue Zeile links beginnend)
3) wieder moeglichst kleine Zahl eintragen, falls Feld schon belegt wird das Feld nicht
   in das Set aufgenommen, damit diese spaeter nicht entfernt werden
4) Gibt es nicht eine moeglichkeit eine Zahl einzutragen geht man zum letzten Feld und setzt
   dort die naechste moegliche Zahl
5) Wiederholen bis das Sudoku geloest ist

old variant (using a lot of copy.deepcopy): 231
new variant (without deepcopy): doesn't work :(
"""
import copy
import time


def main():
    sudokus = read_sudoku_data('096_sudoku.txt')

    valid = True
    for y in range(9):
        for x in range(9):
            t1 = line_rule((x, y), sudokus[0])
            t2 = row_rule((x, y), sudokus[0])
            t3 = square_rule((x, y), sudokus[0])
            if not (t1 and t2 and t3):
                valid = False
    print('valid', valid)

    result = 0
    count = 0
    for sudoku in sudokus:
        t0 = time.time()
        print('now solving sudoku: ', count)
        solved_sudoku = solve(sudoku)
        result += (solved_sudoku[0][0] * 100) + (solved_sudoku[0][1] * 10) + (solved_sudoku[0][2] * 1)
        print('needed time:', time.time() - t0)
        count += 1
    print('wanted num:', result)


def solve(sudoku):
    x, y = 0, 0
    solved, sudoku = next_step((x,y), copy.deepcopy(sudoku))
    if not solved:
        print('!!!!!!!!!!!!!!!!! --- Sudoku has no valid solution! --- !!!!!!!!!!!!!!!!!!!!')
    return sudoku


def next_step(next_field: tuple, sudoku):
    x, y = next_field

    # from start given number -> go to next
    if sudoku[y][x] != 0:
        # last field is filled -> sudoku is solved
        if x == 8 and y == 8:
            return True, sudoku
        # skip field because it's already filled
        else:
            return next_step(increase_pos(x, y), sudoku)

    tmp_sudoku = copy.deepcopy(sudoku)
    # test every num for this field
    for num in range(1, 10):
        tmp_sudoku[y][x] = num
        t1 = row_rule((x, y), tmp_sudoku)
        t2 = line_rule((x, y), tmp_sudoku)
        t3 = square_rule((x, y), tmp_sudoku)
        if t1 and t2 and t3:
            if x == 8 and y == 8:
                return True, tmp_sudoku
            else:
                solved, s = next_step(increase_pos(x, y), tmp_sudoku)
                if solved:
                    return True, s
                elif num == 9:
                    return False, s
                else:
                    continue

    # field couldn't find a valid solution -> return False
    return False, tmp_sudoku


def new_next_step(next_field: tuple, sudoku):
    x, y = next_field

    # from start given number -> go to next
    if sudoku[y][x] != 0:
        # last field is filled -> sudoku is solved
        if x == 8 and y == 8:
            return True, sudoku
        # skip field because it's already filled
        else:
            return new_next_step(increase_pos(x, y), sudoku)

    # test every num for this field
    for num in range(1, 10):
        sudoku[y][x] = num
        t1 = row_rule((x, y), sudoku)
        t2 = line_rule((x, y), sudoku)
        t3 = square_rule((x, y), sudoku)
        if t1 and t2 and t3:
            if x == 8 and y == 8:
                return True, sudoku
            else:
                solved, s = new_next_step(increase_pos(x, y), sudoku)
                if solved:
                    return True, s
                elif num == 9:
                    return False, s
                else:
                    continue

    # field couldn't find a valid solution -> return False
    sudoku[y][x] = 0
    return False, sudoku


def increase_pos(x, y):
    if x == 8 and y == 8:
        print("max pos already reached, can't increase further!")
    x += 1
    if x == 9:
        x = 0
        y += 1
    return x, y


def line_rule(new_num_pos, sudoku):
    y = new_num_pos[1]

    # index is num and value is occuring in line
    check = [False for _ in range(10)]
    for x in range(9):
        if sudoku[y][x] == 0:
            continue
        elif check[sudoku[y][x]]: # double occuring isnt allowed
            return False
        else:
            check[sudoku[y][x]] = True
    return True


def row_rule(new_num_pos, sudoku):
    x = new_num_pos[0]

    # index is num and value is occuring in line
    check = [False for _ in range(10)]
    for y in range(9):
        if sudoku[y][x] == 0:
            continue
        elif check[sudoku[y][x]]:  # double occuring isnt allowed
            return False
        else:
            check[sudoku[y][x]] = True
    return True


def square_rule(new_num_pos, sudoku):
    """
    expect new_num_pos as (x, y) and 1<=x<=9  equally for y
    """

    x, y = new_num_pos
    x = (x // 3) * 3
    y = (y // 3) * 3
    check = [False for _ in range(10)]

    for i in range(y, y+3):
        for j in range(x, x+3):
            if sudoku[i][j] == 0:
                continue
            elif check[sudoku[i][j]]:  # double occurring isn't allowed
                return False
            else:
                check[sudoku[i][j]] = True
    return True


def read_sudoku_data(filename):
    data_file = open(filename)
    sudokus = []
    i = 0
    for line in data_file.readlines():
        if i == 0:
            sudoku = []
            i += 1
            continue

        sudoku.append([int(x) for x in line.strip()])

        if i == 9:
            sudokus.append(sudoku)
        i += 1
        i %= 10
    return sudokus


def print_sudoku(sudoku):
    i = 1
    print("-------------------------------")
    for line in sudoku:
        print('| {}  {}  {} | {}  {}  {} | {}  {}  {} |'.format(*line))
        if i % 3 == 0:
            print("-------------------------------")
        i += 1


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
