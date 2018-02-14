"""
idea:

for larger n's the difference between P_n and P_n+1 increases

starting with all small pairs working up

"""
import time


def main():

    pentagonals = [get_pentagonal(num) for num in range(1, 10000)]

    pentagonals_set = set(pentagonals)

    smallest_difference = 1000000000

    for i in range(len(pentagonals)):
        for j in range(i, len(pentagonals)):
            if i == j:
                continue

            difference = pentagonals[j] - pentagonals[i]
            if (pentagonals[i] + pentagonals[j]) in pentagonals_set \
                    and difference in pentagonals_set:
                if difference < smallest_difference:
                    smallest_difference = difference
                    print(smallest_difference)

    print("smallest found:", smallest_difference)


def get_pentagonal(n):
    return n * (3*n - 1) / 2


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
