"""
Task:


"""
import time


def main():

    primes = set(all_primes(1000000))

    wanted_nums = []

    for prime in primes:
        prime_str = str(prime)
        is_truncatable = True
        for i in range(1, len(prime_str)):
            if int(prime_str[i:]) not in primes:
                is_truncatable = False
            if int(prime_str[:len(prime_str)-i]) not in primes:
                is_truncatable = False

        if is_truncatable:
            wanted_nums.append(prime)

    wanted_nums.remove(2)
    wanted_nums.remove(3)
    wanted_nums.remove(5)
    wanted_nums.remove(7)

    print(wanted_nums)
    print("len", len(wanted_nums))
    print(sum(wanted_nums))


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