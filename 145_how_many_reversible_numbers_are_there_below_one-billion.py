"""
idea:
"""
import time


def main():
    limit = 10**8 # no number between 10^8 and 10^9 satisfies condition
    found = set()

    next_num_len = 100
    num_len = 2
    for i in range(10, limit):
        if i % 100000 == 0:
            print(i/limit * 100, '%')
        if i == next_num_len: # keep track how many digits i has
            next_num_len *= 10
            num_len += 1
        if i in found:
            continue
        elif i % 10 == 0: # leading zeroes on reverse number aren't allowed
            continue
        else:
            num1 = i
            num2 = i
            carry = 0
            digit_pos = num_len - 1
            all_odd = True
            rev = 0
            while num1 > 0:
                s = (num2 // 10**digit_pos) + (num1 % 10) + carry
                digit = s % 10
                if digit % 2 == 0:
                    all_odd = False
                    break
                carry = s // 10
                rev = rev + ((num1 % 10) * 10**digit_pos)
                digit_pos -= 1
                num1 //= 10
                num2 %= 10**(digit_pos+1)
            if all_odd and (carry % 2 == 1 or carry == 0):
                found.add(i)
                found.add(rev)

            # rev = int(str(i)[::-1])
            # num_sum = i + rev
            # all_odd = True
            # while num_sum >= 10:
            #     digit = num_sum % 10
            #     if digit % 2 == 0:
            #         all_odd = False
            #         break
            #     num_sum //= 10
            # if all_odd:
            #     found.add(i)
            #     found.add(rev)

    print('counted nums:', len(found))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
