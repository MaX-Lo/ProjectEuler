"""
Task:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.


"""
import time


def main():
    start_time = time.time()

    limit = 2000000

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
            if not numbers[i]:
                p = i
                numbers[i] = True
                primes.append(i)
                break
            else:
                p += 1

    #print(primes)
    print("sum of found primes:", sum(primes))
    print("time:", time.time() - start_time)


if __name__ == '__main__':
    main()
