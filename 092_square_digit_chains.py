"""
idea:
"""
import time


def main():
    nums89 = 0

    ender89 = set()

    for num in range(1, 10000000):
        if num % 100000 == 0:
            print("progress:", num, "89 nums:", nums89)
        curr = num
        while curr != 1:
            curr = digit_square(curr)
            if curr in ender89 or curr == 89:
                ender89.add(num)
                nums89 += 1
                break

    # old time: 127.95 and result: 8581145 (+1) (testing until 89)
    # new time: 047.18 and result: 8581146      (storing found nums in set)
    print("final result:", nums89)


def digit_square(num):
    res = 0
    for c in str(num):
        res += int(c)**2
    return res


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
