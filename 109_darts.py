"""
idea:
"""
import time


def main():
    solution()


def solution():
    singles = {'S{}'.format(str(x)): x for x in range(1, 21)}
    doubles = {'D{}'.format(str(x)): x * 2 for x in range(1, 21)}
    doubles['DB'] = 50
    triples = {'T{}'.format(str(x)): x * 3 for x in range(1, 21)}
    specials = {'B25': 25, 'N0': 0}

    print(singles)
    scores = {**singles, **doubles, **triples, **specials}

    count = 0

    for checkout_with in range(2, 100):
        found = set()
        tmp_count = 0
        for score3 in doubles:
            remaining = checkout_with - doubles[score3]
            for score2 in scores:
                first = remaining - scores[score2]
                for score1 in scores:
                    if scores[score1] == first:
                        combination = frozenset({score1, score2})
                        if combination not in found:
                            #print(score1, score2, score3)
                            tmp_count += 1
                            found.add(combination)
        count += tmp_count
        print('checkout with {}, counted: {}'.format(checkout_with, tmp_count))

    print('counted {} combinations'.format(count))

    print(scores)



if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
