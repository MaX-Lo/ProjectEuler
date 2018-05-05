"""
idea:
"""
import time


def main():
    solution()

def solution():
    res = 0

    for a in range(3, 1001):
        r_max = 0
        n_max = 0
        for n in range(1, a+a):
            r = f(a, n)
            if r > r_max:
                r_max = r
                n_max = n
        print('a', a, 'r max', r_max, ' at n', n_max)
        res += r_max
    print('end sum', res)

def f(a, n):
    # improvement: after every power modulo
    # mod = a**2
    # a1, a2 = a-1, a+1
    # r1, r2 = a1, a2
    # for i in range(1, n):
    #     r1, r2 = r1*a1%mod, r2*a2%mod
    # return r1 + r2
    return ((a-1)**n + (a+1)**n) % a**2


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
