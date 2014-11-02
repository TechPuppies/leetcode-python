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

    def breakpoint(self, num):
        """ find the break point num[i] < num[i+1] """
        p = len(num) - 2
        while p >= 0:
            if num[p] < num[p + 1]:
                return p
            p -= 1 # forgot this f**king shit again!!!!!!!!
        return None

    def autoswap(self, num, breakpoint):
        """
        swap breakpoint with the smallest larger num
        then reverse everything after it
        """
        for i in range(breakpoint + 1, len(num) - 1):
            if num[breakpoint] > num[i + 1]:
                num[breakpoint], num[i] = num[i], num[breakpoint]
                s, e = i + 1, len(num) - 1
                while e > s:
                    num[s], num[e] = num[e], num[s]
                return
        num[breakpoint], num[-1] = num[-1], num[breakpoint]

    def nextPermutation(self, num):
        breakpoint = self.breakpoint(num)
        if not breakpoint:
            num.reverse()
        else:
            self.autoswap(num, breakpoint)
        return num


class Test(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test(self):
        self.assertEqual(
            self.s.nextPermutation([1, 2]), [2, 1])
        self.assertEqual(
            self.s.nextPermutation([2, 1]), [1, 2])
        self.assertEqual(
            self.s.nextPermutation([1, 2, 3]), [1, 3, 2])
        self.assertEqual(
            self.s.nextPermutation([3, 2, 1]), [1, 2, 3])
        self.assertEqual(
            self.s.nextPermutation([1, 1, 5]), [1, 5, 1])
        self.assertEqual(
            self.s.nextPermutation([1, 9, 4, 7]), [1, 9, 7, 4])


if __name__ == '__main__':
    unittest.main()
