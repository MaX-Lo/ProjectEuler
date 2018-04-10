"""
idea:

alle permutationen testen

"""
import time

import primesieve


def main():
    version2()


def version2():
    primes = [str(prime) for prime in primesieve.primes(10000)]
    prime_set = set(primesieve.primes(100000000))

    for i1 in range(len(primes)):
        for i2 in range(i1+1, len(primes)):
            if not (int(primes[i1]+primes[i2]) in prime_set) or not (int(primes[i2]+primes[i1]) in prime_set):
                continue
            for i3 in range(i2+1, len(primes)):
                if not (int(primes[i1] + primes[i3]) in prime_set) or not (int(primes[i2] + primes[i3]) in prime_set) \
                        or not (int(primes[i3] + primes[i1]) in prime_set) or not (int(primes[i3] + primes[i2]) in prime_set):
                    continue
                for i4 in range(i3+1, len(primes)):
                    if not (int(primes[i1] + primes[i4]) in prime_set) \
                            or not (int(primes[i2] + primes[i4]) in prime_set) \
                            or not (int(primes[i3] + primes[i4]) in prime_set) \
                            or not (int(primes[i4] + primes[i1]) in prime_set) \
                            or not (int(primes[i4] + primes[i2]) in prime_set) \
                            or not (int(primes[i4] + primes[i3]) in prime_set):
                        continue
                    # print("found 4:", primes[i1], primes[i2], primes[i3], primes[i4])

                    for i5 in range(i4+1, len(primes)):
                        if not (int(primes[i1] + primes[i5]) in prime_set) \
                                or not (int(primes[i2] + primes[i5]) in prime_set) \
                                or not (int(primes[i3] + primes[i5]) in prime_set) \
                                or not (int(primes[i4] + primes[i5]) in prime_set) \
                                or not (int(primes[i5] + primes[i1]) in prime_set) \
                                or not (int(primes[i5] + primes[i2]) in prime_set) \
                                or not (int(primes[i5] + primes[i3]) in prime_set) \
                                or not (int(primes[i5] + primes[i4]) in prime_set):
                            continue

                        print("found 5:", primes[i1], primes[i2], primes[i3], primes[i4], primes[i5])
                        added = int(primes[i1]) + int(primes[i2]) + int(primes[i3]) + int(primes[i4]) + int(primes[i5])
                        print("sum", added)
                        return


def version1():

    primes = [str(prime) for prime in primesieve.primes(10000000)]
    prime_set = set(primesieve.primes(10000000))

    i1, i2, i3, i4, i5 = 0, 1, 2, 3, 4  # indexes in prime list
    s = [str(2), str(3), str(5), str(7), str(11)]
    found = False
    i = 0
    while not found:
        i += 1
        if i % 100000 == 0:
            print("progress:", primes[i5])

        if i1 == i2:
            i1 = 0
            i2 += 1
            s[0] = primes[i1]
            s[1] = primes[i2]
        if i2 == i3:
            i2 = 1
            i3 += 1
            s[1] = primes[i2]
            s[2] = primes[i3]
        if i3 == i4:
            i3 = 2
            i4 += 1
            s[2] = primes[i3]
            s[3] = primes[i4]
        if i4 == i5:
            i4 = 3
            i5 += 1
            s[3] = primes[i4]
            s[4] = primes[i5]

        no = False
        for j1 in range(5):
            for j2 in range(1, 5+1):
                if j1 == (j1+j2)%5:
                    continue
                if not (int(s[j1] + s[(j1+j2)%5]) in prime_set):
                    no = True
                    break
            if no:
                break

        if not no:
            found = True
            print("Found:", s[0], s[1], s[2], s[3], s[4])

        i1 += 1
        s[0] = primes[i1]


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
