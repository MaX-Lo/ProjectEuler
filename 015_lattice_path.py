"""
Task:


"""
import time


def main():
    start_time = time.time()

    size = 14
    # print("fast version: ", go2(size, size))
    # print("time:", time.time() - start_time)
    table = create_table(21, 21)

    print(table[20, 20])
    print("time:", time.time() - start_time)


def go(x, y, max_x, max_y):
    count = 0
    if x == max_x and y == max_y:
        return 1
    if x < max_x:
        count += go(x+1, y, max_x, max_y)
    if y < max_y:
        count += go(x, y+1, max_x, max_y)
    return count


def go2(x, y):
    if x == 1:
        return y+1
    if y == 1:
        return x+1
    else:
        return go2(x-1, y) + go2(x, y-1)


def create_table(max_x, max_y):
    table = {}
    for x in range(1, max_x):
        table[(1, x)] = x + 1
        table[(x, 1)] = x + 1

    for x in range(2, max_x):
        for y in range(2, x+1):
            table[(y, x)] = table[((x-1), y)] + table[(x, (y-1))]
            table[(x, y)] = table[((x-1), y)] + table[(x, (y-1))]
    return table


if __name__ == '__main__':
    main()
