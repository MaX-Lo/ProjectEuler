"""
idea:


"""
import time


def main():

    limit = 10000000

    num_str = ''
    i = 1
    while i < limit:
        if i % 1000 == 0: # stop if len is already of
            if len(num_str) > limit:
                break
        num_str += str(i)
        i += 1

    product = 1
    for i in [9, 99, 999, 9999, 99999, 999999]:
        product *= int(num_str[i])

    print(product)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)