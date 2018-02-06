"""
Task:


"""
import time


def main():

    power = 5

    ls = []

    for i in range(2, 354294+1): # 354294 is the biggest number creatable by 6 * 9^5
        if i % 50000 == 0:
            print("current pos -->", i)
        txt = str(i)
        digit_power_sum = 0
        for digit in txt:
            digit_power_sum += int(digit)**power
        if digit_power_sum == i:
            ls.append(i)
            print(i)

    print("wanted nums:", ls)
    print("sum of wanted nums:", sum(ls))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
