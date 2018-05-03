"""
idea:
"""
import copy
import time

# 122106096, 5453760

def main():
    max_row_len = 50
    print('row length:', max_row_len)

    if max_row_len % 2 == 0:
        start = 2
        combinations = 1
    else:
        combinations = 0
        start = 1

    for gaps in range(start, max_row_len-1, 2): # step 2 because only even num of gaps is possible
        tmp_combinations = get_gap_combinations(gaps, max_row_len)
        combinations += tmp_combinations
        # print('gaps', gaps, 'combs', tmp_combinations)

    print('all combinations for block len 2:', combinations)


def increasing_nums(nums, max_num):
    max_num += 1
    count = {i: 1 for i in range(max_num)}

    for i in range(1, nums):
        tmp_count = {}
        for num in range(max_num):
            tmp_count[num] = 0
            for j in range(num, max_num):
                tmp_count[num] += count[j]

        count = copy.deepcopy(tmp_count)

    res = 0
    for num in count:
        res += count[num]
    return res


def get_gap_combinations(gaps, row_len):
    if (row_len-gaps) % 2 != 0:
        print("blocks can't be even")
    max_jumps = (row_len - gaps) // 2
    return increasing_nums(gaps, max_jumps)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)