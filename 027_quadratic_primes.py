"""
Task:


"""
import time


def main():

    primes = set(all_primes(1000000))
    largest_precalculated_prime = max(primes)
    print("primes: check")

    max_a = -1
    max_b = -1
    max_primes = -1

    for a in range(-999, 1000): #range(-999, 1000):
        print(a)
        for b in range(-1000, 1001): #range(-1000, 1001):
            n = 0
            x = n**2 + n + 41
            while x <= largest_precalculated_prime and x in primes:
                n += 1
                x = n**2 + a*n + b
            if n > max_primes:
                max_primes = n
                max_a = a
                max_b = b

    print("a:", max_a, "b:", max_b, "a*b=", max_a*max_b, "max consecutives primes:", max_primes)


def all_primes(limit):
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
    return primes


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)