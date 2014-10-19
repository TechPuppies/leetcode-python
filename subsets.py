# coding=utf-8
# AC Rate: 27.9%
# SOURCE URL: https://oj.leetcode.com/problems/subsets/
#
#
# Given a set of distinct integers, S, return all possible subsets.
#
# Note:
#
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
#
#
#
# For example,
# If S = [1,2,3], a solution is:
#
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#
#
import unittest

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        # return self.helper(S, 0)
        # change it into bottom up
        start = [[]]
        for i in range(len(S))[::-1]:
            res = []
            for j in start:
                res.append([S[i]] + j)
                res.append(j)
            start = res
        return start

    # def helper(self, S, i):
    #     if i >= len(S):
    #         return [[]]
    #     si1 = self.helper(S, i+1)
    #     # no point to dp
    #     return [[S[i]] + ss for ss in si1] + \
    #         [ss for ss in si1]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.subsets([1,2,3]),
            [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []])

if __name__ == '__main__':
    unittest.main()
