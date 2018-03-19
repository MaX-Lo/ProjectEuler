"""
idea:
"""
import time


def main():
    v2(100)


def v2(limit):
    print(count(limit-1, limit))


def count(curr_num, remaining):
    if remaining < 0:
        return 0
    if remaining == 0:
        return 1

    possibilities = 0
    for i in range(1, curr_num+1):
        possibilities += count(i, remaining-i)

    return possibilities


def v1():
    limit = 7

    a = [[x for x in range(limit + 1)]]
    line1 = [0]
    line1.extend([1 for x in range(limit)])
    a.append(line1)

    for i in range(2, limit):
        line = [0]
        printm(a)
        for j in range(1, limit + 1):
            if j < i:
                val = a[-1][j]
            elif j % i == 0:
                diff = line[j - 1] - a[-1][j - 1]
                val = a[-1][j] + 1 + diff
            else:
                r = j % i
                print('r:', r, line[j - r], (a[-1][r] - 1), (a[-1][j] - a[-1][j - r]))
                val = line[j - r] + (a[-1][r] - 1) + (a[-1][j] - a[-1][j - r])
            line.append(val)
            print(line, '.', i, j)
        a.append(line)

    printm(a)
    print('size', limit)

def printm(matrix):
    print('----')
    for line in matrix:
        print(line)
    print('----')


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)