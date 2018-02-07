"""
idea:


"""
import time


def main():

    # one million
    # 78498
    # time: 0.7800731658935547 new 0.6487257480621338
    # ten million
    # 664579
    # time: 8.014394760131836
    primes = all_primes(10000000)
    print(primes)
    print(len(primes))

    pass


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


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_set.append(line.strip())
    return data_set


