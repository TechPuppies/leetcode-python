# coding=utf-8
# AC Rate: 25.4%
# SOURCE URL: https://oj.leetcode.com/problems/next-permutation/
#
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
#
#
# If such arrangement is not possible, it must rearrange it as the
# lowest possible order (ie, sorted in ascending order).
#
#
# The replacement must be in-place, do not allocate extra memory.
#
#
# Here are some examples. Inputs are in the left-hand column and
# its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#
import unittest


class Solution:
    # @param num, a list of integer
    # @return a list of integer

    def nextPermutation(self, num):
        if len(num) < 2:
            return num

        p1 = len(num) - 2
        while p1 >= 0:
            p2 = len(num) - 1
            while p2 > p1:
                if num[p1] < num[p2]:
                    num[p1], num[p2] = num[p2], num[p1]
                    num[p1 + 1:] = num[p1 + 1:][::-1]
                    return num
                p2 -= 1
            p1 -= 1
        return num[::-1]


class Test(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_123(self):
        self.assertEqual(
            self.s.nextPermutation([1, 2, 3]), [1, 3, 2])

    def test_321(self):
        self.assertEqual(
            self.s.nextPermutation([3, 2, 1]), [1, 2, 3])

    def test_115(self):
        self.assertEqual(
            self.s.nextPermutation([1, 1, 5]), [1, 5, 1])


if __name__ == '__main__':
    unittest.main()
