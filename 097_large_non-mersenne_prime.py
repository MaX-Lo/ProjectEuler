"""
idea:


"""
import time


def main():
    num = 28433*powermod(2, 7830457, 10000000000)+1

    print(num)


def powermod(base, exp, mod):
    num = base
    while exp > 1:
        num = num * base % mod
        exp -= 1
    return num


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
