"""
Task:


"""
import time

import math


def main():

    a = 300
    b = 400
    c = 500

    sum_probabilities = 0
    num_of_checks = 0

    for a_new in range(1, a+1):
        for b_new in range(1, b+1):
            if a_new+b_new <= c:
                continue

            num_of_checks += 1
            #print("angle", math.acos((c**2-a_new**2-b_new**2)/(-2*a_new*b_new)))
            probability = math.acos((c**2-a_new**2-b_new**2)/(-2*a_new*b_new)) / (2*math.pi)
            sum_probabilities += probability
        print(a_new)

    print("average prob", sum_probabilities / num_of_checks)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)