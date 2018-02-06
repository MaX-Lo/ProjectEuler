"""
Task:


"""
import time


def main():
    start_time = time.time()

    a = 1
    amicable_numbers = []
    while a < 10000:
        if a % 100 == 0:
            print(a)

        d_a = sum(get_divisors(a))
        d_b = sum(get_divisors(d_a))
        if a == d_b:
            if not (a, d_a) in amicable_numbers and not (d_a, a) in amicable_numbers and a != d_a:
                amicable_numbers.append((a, d_a))
        a += 1

    summ = 0
    for a, b in amicable_numbers:
        summ += a + b

    print(amicable_numbers)
    print("sum of amicable numbers:", summ)

    print("time:", time.time() - start_time)


def get_divisors(n):
    divisors = []
    for i in range(int(n/2), 0, -1):
        if (n / i).is_integer():
            divisors.append(i)
    return divisors


if __name__ == '__main__':
    main()