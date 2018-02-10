def all_primes(limit):
    segment_size = 20000000

    if limit <= segment_size:
        return primes_euklid(limit)

    primes = primes_euklid(segment_size)

    iteration = 1
    while limit > segment_size * iteration:
        print("progress, at:", segment_size * iteration)

        start = segment_size*iteration
        end = segment_size * (iteration + 1)
        primes = segmented_primes(start, end, primes)
        iteration += 1

    start = segment_size*iteration
    end = limit

    if start == end:
        return primes
    else:
        return segmented_primes(start, end, primes)


def primes_euklid(limit):
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


def segmented_primes(n, limit, primes):
    """
    :param n: start value to search for primes
    :param limit: end value to search for primes
    :param primes: primes smaller than n
    :return:
    """

    if n % 2 == 0:
        n -= 1

    # create dict with numbers in that segment
    numbers = {}
    for x in range(n, limit, 2):
        numbers[x] = False

    # Todo marking takes like forever...
    # mark all numbers that are multiples of primes in the given list of primes for smaller numbers
    for num in numbers:
        for prime in primes:
            if num % prime == 0:
                numbers[num] = True
            if numbers[num]:
                break

    # find the first prime in this segment to start with
    p = -1
    for num in numbers:
        if not numbers[num]:
            p = num
            primes.append(p)
            break
    if p == -1:
        print("Error, no prime in segment found...")

    # sieve primes in the segment
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
                p += 2

    return primes