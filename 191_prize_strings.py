"""
idea:
"""
import time


def main():
    solution()


def solution():
    length = 30

    OX_L = 2
    AO_L = 1
    AA_L = 1
    LX_nL = 2
    OX_nL = 1
    AOorL_nL = 1  # A followed by O or L with L already used
    AA_nL = 0

    for l in range(2, length):
        new_OX_L = OX_L + AO_L + AA_L
        new_AO_L = OX_L
        new_AA_L = AO_L

        new_LX_nL = OX_L + AO_L + AA_L
        new_OX_nL = OX_nL + AOorL_nL + AA_nL + LX_nL
        new_AOorL_nL = OX_nL + LX_nL
        new_AA_nL = AOorL_nL

        OX_L = new_OX_L
        AO_L = new_AO_L
        AA_L = new_AA_L
        LX_nL = new_LX_nL
        OX_nL = new_OX_nL
        AOorL_nL = new_AOorL_nL
        AA_nL = new_AA_nL

        # print('OX_L:    ', OX_L)
        # print('AO_L:    ', AO_L)
        # print('AA_L:    ', AA_L)
        # print('LX_nL:   ', LX_nL)
        # print('OX_nL:   ', OX_nL)
        # print('AOorL_nL:', AOorL_nL)
        # print('AA_nL:   ', AA_nL)

    answer = OX_L + AO_L + AA_L + LX_nL + OX_nL + AOorL_nL + AA_nL
    print('counted', answer)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
