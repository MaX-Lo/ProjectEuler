"""
idea:

How functions are written:
f(x) = a + b*x + c*x^2 + d*x^3
gets written as [a, b, c, d]
the corresponding exponents can be deduced from the length of that list
"""

import time
import numpy as np


def main():
    fit_sum = 0

    generating_polynomial = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
    #generating_polynomial = [0, 0, 0, 1]
    degree = len(generating_polynomial)
    values = [eval_polynomial(x, generating_polynomial) for x in range(1, degree+1)]

    for k in range(1, degree+1):
        value_pairs = [(x+1, values[x]) for x in range(k)]
        polynomial = find_polynomial(value_pairs)
        i = 1
        while i <= degree:
            val = eval_polynomial(i, polynomial)
            real_val = eval_polynomial(i, generating_polynomial)
            if val != real_val:
                fit_sum += val
                break
            i += 1

    print('num:', fit_sum)


def find_polynomial(values):
    """ find the simplest matching polynomial to the given value pairs
        given as [(x1, y1), (x2, y2), ...]

        write arising equations as matrices

        X = [a, b, c, d, ...]^T
        A = [f(x1), f(x2), ...]^T
        B = [y1, y2, y3, ...]^T

        A*X=B  ->  A^-1 * A*X = A^-1*B  ->  X = A^-1 * B
    """
    degree = len(values) - 1
    equations = []
    results = []
    for x, y in values:
        equation = [x**i for i in range(degree + 1)]
        equations.append(equation)
        results.append([y])

    a = np.matrix(equations)
    b = np.matrix(results)
    a_inverse = np.linalg.inv(a)
    x = a_inverse * b
    # print('a')
    # print(a)
    # print('b')
    # print(b)
    # print('x')
    # print(x)
    polynomial = [int(round(num)) for numl in x.tolist() for num in numl]
    return polynomial


def eval_polynomial(x, polynomial):
    """
    return the value of polynomial(x)

    """

    curr_exp = 0
    value = 0
    for factor in polynomial:
        value += factor * x**curr_exp
        curr_exp += 1
    return value


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)