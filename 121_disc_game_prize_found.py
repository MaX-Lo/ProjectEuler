"""
idea:
"""
import time

import math


def main():
    turns = 15

    needed_ones = turns // 2 + 1

    chance_sum = 0

    for i in range(2**turns):
        binary = bin(i)[2:]
        if len(binary) < turns:
            binary = '0'*(turns - len(binary)) + binary

        ones = binary.count('1')
        if ones >= needed_ones:
            chance = 1
            for pos in range(turns):
                if binary[pos] == '1':
                    chance *= 1 / (pos + 2)
                else:
                    chance *= (pos + 1) / (pos + 2)
            print(binary, chance)
            chance_sum += chance

    print('chance', chance_sum)
    print('win', math.floor(1/chance_sum))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
