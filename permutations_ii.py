# coding=utf-8
# AC Rate: 25.0%
# SOURCE URL: https://oj.leetcode.com/problems/permutations-ii/
#
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
#
#
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].
#
#
import unittest


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        # first is still using DFS
        # let's do recursion
        res = []
        num.sort()
        self.helper(num, 0, res)
        return res

    def helper(self, num, start, res):
        if start >= len(num):
            res.append(num)
        for i in range(start, len(num)):
            if i < 1 or num[i] != num[i-1]:
                num[i], num[start] = num[start], num[i]
                self.helper(num, start + 1, res)
                num[i], num[start] = num[start], num[i]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        print s.permuteUnique([1, 2, 2])

if __name__ == '__main__':
    unittest.main()
