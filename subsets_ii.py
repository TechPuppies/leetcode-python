# coding=utf-8
# AC Rate: 26.9%
# SOURCE URL: https://oj.leetcode.com/problems/subsets-ii/
#
#
# Given a collection of integers that might contain duplicates, S, return all possible subsets.
#
# Note:
#
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
#
#
#
# For example,
# If S = [1,2,2], a solution is:
#
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#
#
import unittest

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        # return self.helper(S, 0)
        # change it into bottom up
        if not S:
            return None
        S.sort()
        start, added = [[], [S[-1]]], 1
        for i in range(len(S) - 1)[::-1]:
            res = []
            k = -added if S[i] == S[i+1] else 0
            for j in start:
                res.append(j)
            for j in start[k:]:
                res.append([S[i]] + j)

            if not S[i] == S[i+1]:
                added = len(start)
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
        self.assertEqual(s.subsetsWithDup([1,2,3]),
            [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]])
        self.assertEqual(s.subsetsWithDup([1,2,2]),
            [[], [2], [2, 2], [1], [1, 2], [1, 2, 2]])
        self.assertEqual(s.subsetsWithDup([1,1,2]),
            [[], [2], [1], [1, 2], [1, 1], [1, 1, 2]])

if __name__ == '__main__':
    unittest.main()
