"""
idea:
"""
import time

import itertools


def main():
    max_consecutive = 0
    max_config = tuple()

    a = 1
    b = 2
    c = 3
    d = 4
    while True:
        if a == b:
            a = 1
            b += 1
        if b == c:
            b = 2
            c += 1
        if c == d:
            c = 3
            d += 1

        target_nums = get_possible_target_nums(a, b, c, d)
        consecutive = count_consecutive(target_nums)
        if max_consecutive < consecutive:
            max_consecutive = consecutive
            max_config = a, b, c, d

        print('consecutive: {} (max {}), a,b,c,d: {} {} {} {} (max {})'.format(consecutive, max_consecutive, a, b, c, d, max_config))

        a += 1


def count_consecutive(target_nums):
    count = 0
    curr = 1
    while True:
        if curr in target_nums:
            count += 1
            curr += 1
        else:
            return count


def get_possible_target_nums(a, b, c, d):
    # contains all numbers that can be generated
    found_targets = set()

    for perm in list(itertools.permutations([a, b, c, d])):
        n1, n2, n3, n4 = perm
        operations = ['*', '/', '+', '-']
        for x1 in operations:
            for x2 in operations:
                for x3 in operations:
                    expressions = ['n1{}n2{}n3{}n4'.format(x1, x2, x3),
                                   '(n1{}n2){}n3{}n4'.format(x1, x2, x3),
                                   '(n1{}n2{}n3){}n4'.format(x1, x2, x3),
                                   'n1{}(n2{}n3){}n4'.format(x1, x2, x3),
                                   'n1{}(n2{}n3{}n4)'.format(x1, x2, x3),
                                   'n1{}n2{}(n3{}n4)'.format(x1, x2, x3),
                                   '(n1{}n2){}(n3{}n4)'.format(x1, x2, x3)]
                    for expression in expressions:
                        #print(expression.replace('n1', str(n1)).replace('n2', str(n2)).replace('n3', str(n3)).replace('n4', str(n4)), eval(expression))
                        try:
                            res = eval(expression)
                            if res % 1 == 0 and res > 0:
                                found_targets.add(res)
                        except ZeroDivisionError:
                            continue

    return found_targets


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
