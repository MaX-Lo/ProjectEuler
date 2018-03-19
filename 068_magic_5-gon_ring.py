"""
idea:
"""
import time


def main():

    brute_force()


def brute_force():
    """
    pretty much testing every possible combination
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i1 in range(len(nums)):
        a = nums[i1]
        nums1 = list(nums)
        nums1.pop(i1)
        for i2 in range(len(nums1)):
            b = nums1[i2]
            nums2 = list(nums1)
            nums2.pop(i2)
            for i3 in range(len(nums2)):
                c = nums2[i3]
                nums3 = list(nums2)
                nums3.pop(i3)
                for i4 in range(len(nums3)):
                    d = nums3[i4]
                    nums4 = list(nums3)
                    nums4.pop(i4)
                    for i5 in range(len(nums4)):
                        e = nums4[i5]
                        nums5 = list(nums4)
                        nums5.pop(i5)
                        for i6 in range(len(nums5)):
                            f = nums5[i6]
                            nums6 = list(nums5)
                            nums6.pop(i6)
                            for i7 in range(len(nums6)):
                                g = nums6[i7]
                                nums7 = list(nums6)
                                nums7.pop(i7)
                                for i8 in range(len(nums7)):
                                    h = nums7[i8]
                                    nums8 = list(nums7)
                                    nums8.pop(i8)
                                    i = nums8[0]

                                    if (f+a+e) == (d+e+i) == (c+d+10) == (b+c+h) == (g+b+a):
                                        print('------')
                                        print(h, c, b)
                                        print(g, b, a)
                                        print(f, a, e)
                                        print(i, e, d)
                                        print(10, d, c)
                                        print('------')


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
