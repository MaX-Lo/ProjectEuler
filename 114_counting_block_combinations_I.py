"""
idea:
"""
import copy
import time
import math


def main():
    solution()


def solution():
    max_row_len = 50

    count = 1

    for row_len in range(max_row_len, 2, -1):
        get_block_len_combinations(row_len, 3, [], {})

        for combination in get_block_len_combinations(row_len, 3, [], {}):
            block_count = 0
            for block_len in combination:
                block_count += combination[block_len]

            combination_arrangements = count_distinct_arrangements_of_block_lengths(combination)
            optional_gaps = max_row_len - row_len
            multiple_by_gaps =  optional_gaps*(block_count + 1) + 1
            multiple_by_gaps = ncr(optional_gaps + block_count, optional_gaps)

            print('row len', row_len, 'combination', combination, 'count', combination_arrangements, 'gap mul', multiple_by_gaps)

            count += combination_arrangements * multiple_by_gaps

    print('counted {} arrangements'.format(count))


def ncr(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def count_distinct_arrangements_of_block_lengths(block_len_combination):
    block_count = 0
    for block_len in block_len_combination:
        block_count += block_len_combination[block_len]

    nominator = math.factorial(block_count)
    denominator = 1
    for block_len in block_len_combination:
        denominator *= math.factorial(block_len_combination[block_len])

    return nominator / denominator


def get_block_len_combinations(row_len, min_block_len, combinations: list, combination: dict):
    """
    count the different block length combinations for:
        - a row with length row_len
        - a min block len of min_block_len
        - a gap of exactly 1 between each block

        combination {3: 2, 4: 1} means the row can be filled by 2 times a 3 Block and one 4 Block, between
        each Block is a gap of size one
    """

    for curr_block_len in range(min_block_len, row_len+1):
        #print('curr block len:', curr_block_len, 'row len', row_len)

        curr_combination = copy.deepcopy(combination)
        # add to curr_combinations and continue if there is enough space for a gap
        if row_len - (curr_block_len + 1) >= 0:
            if curr_block_len in curr_combination:
                curr_combination[curr_block_len] += 1
            else:
                curr_combination[curr_block_len] = 1
            remaining_row_len = row_len - (curr_block_len + 1)
            get_block_len_combinations(remaining_row_len, curr_block_len, combinations, curr_combination)
        # remaining space is 0, so add this combination to combinations and continue with a different one
        elif row_len - curr_block_len == 0:
            if curr_block_len in curr_combination:
                curr_combination[curr_block_len] += 1
            else:
                curr_combination[curr_block_len] = 1
            combinations.append(curr_combination)
        else:
            print('that shouldnt happen! cur block len', curr_block_len, ' row len', row_len)
    return combinations


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
