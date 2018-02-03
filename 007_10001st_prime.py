"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import time


def main():
    start_time = time.time()

    limit = 1000000

    # list containing for every number whether it has been marked already
    numbers = {}
    for x in range(3, limit, 2):
        numbers[x] = False

    primes = [2, 3]

    p = 3
    while p < limit:
        for i in range(p, limit, p):
            numbers[i] = True

        for i in range(p, limit, 2):
            if numbers[i] == False:
                p = i
                numbers[i] = True
                primes.append(i)
                if (len(primes)==10001):
                    print("10001st prime:", p)
                break
            else:
                p += 1

    print(primes)
    print("number of found primes:", len(primes))
    print("time:", time.time() - start_time)





if __name__ == '__main__':
    main()