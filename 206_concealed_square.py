"""
idea:
"""
import time

import math


def main():
    length = 19
    num = int(math.sqrt(10 ** (length - 1)))
    num_str = str(num ** 2)

    while not ((num_str[0] == '1') and (num_str[2] == '2') and (num_str[4] == '3')
               and (num_str[6] == '4') and (num_str[8] == '5') and (num_str[10] == '6')
               and (num_str[12] == '7') and (num_str[14] == '8') and (num_str[16] == '9')
               and (num_str[18] == '0')):
        num += 10
        num_str = str(num ** 2)

        if (1000000000 - num) % 1000000 == 0:
            print(num_str)

    print('found:', num_str)

    pass


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
