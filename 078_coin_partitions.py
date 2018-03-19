"""
idea:
"""
import time


def main():
    pentagonals = generate_pentagonals(100000)

    partitions_ls = [1]
    n = 1
    while partitions_ls[-1] % 1000000 != 0:
        t = 0
        pen_ind = 0
        count = 0
        while n - pentagonals[pen_ind] >= 0:
            if t == 0 or t == 1:
                count += partitions_ls[n - pentagonals[pen_ind]]
            else:
                count -= partitions_ls[n - pentagonals[pen_ind]]
            t += 1
            t %= 4
            pen_ind += 1
        partitions_ls.append(count)
        n += 1

    print(partitions_ls[-1])
    print('n', n-1)


def generate_pentagonals(n_max):
    pentagonals = []
    for i in range(1, n_max+1):
        pentagonals.append(pentagonal(i))
        pentagonals.append(pentagonal(-i))
    return pentagonals


def pentagonal(n):
    return int((3 * n**2 - n) / 2)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
