"""
idea:
"""
import time

import math


def main():
    larger_than = 1#10**12

    b = larger_than / 1.4142131
    r = b * 0.4142131
    b = int(round(b))
    r = int(round(r))

    mysterious_method(10**12)

    count = 0
    while True:
        count += 1
        #if count % 1000000 == 0:
            #print('progress:', count/1000000, 'Mio')
        left = b**2 - b
        right = 2*b*r + r**2 - r
        # print(left, ' = ', right, b, r)
        # print('p = ', (b**2 - b) / ((b+r)**2 - b - r))
        if left == right:
            print('found: b:', b, ' r:', r)
            r += 1
            break
        elif left < right:
            b += 1
        else:
            r += 1

    print('solution is: blue = ', b, 'red = ', r)


def mysterious_method(limit):

    n = 2
    r = 1
    b = 1
    while r + b < limit:
        b, r = curious(n)
        n += 1
        print('sum:', r+b, ' b:', b, ' r:', r)
    print('final solution for b is:', round(b))


def curious(n):
    r2 = math.sqrt(2)
    tp_r = (3 + 2 * r2) ** n
    n += 1
    tp_b = (3 + 2 * r2) ** n
    tm_b = (3 - 2 * r2) ** n

    r = - ((3 - 2 * r2)**n - tp_r / (4*r2))
    b = 1/8 * (2*tm_b + r2*tm_b + 2*tp_b - r2*tp_b + 4)
    return b, r


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)