"""
Task:


"""
import time


def main():
    start_time = time.time()

    print("time:", time.time() - start_time)

    abundant_nums = []
    for i in range(1, 28125):
        if i % 2000 == 0:
            print(i)
        divisors_sum = sum(get_divisors(i))
        if divisors_sum > i:
            abundant_nums.append(i)

    wanted_nums_sum = 0
    creatable_pairs = create_all_permutations(abundant_nums)
    for num in range(1, 28125): # 28123
        if num % 2000 == 0:
            print(num)
        if num not in creatable_pairs:
            wanted_nums_sum += num

    print("wanted nums sum:", wanted_nums_sum)
    print("time:", time.time() - start_time)


def create_all_permutations(abundant_nums):
    creatable_nums = set()
    for ab1 in abundant_nums:
        for ab2 in abundant_nums:
            creatable_nums.add(ab1 + ab2)

    return creatable_nums


def get_divisors(n):
    divisors = []
    for i in range(int(n/2), 0, -1):
        if (n / i).is_integer():
            divisors.append(i)
    return divisors


if __name__ == '__main__':
    main()
