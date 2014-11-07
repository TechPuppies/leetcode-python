# coding=utf-8
# AC Rate: 30.3%
# SOURCE URL: https://oj.leetcode.com/problems/combinations/
#
#
# Given two integers n and k, return all possible
# combinations of k numbers out of 1 ... n.
#
#
# For example,
# If n = 4 and k = 2, a solution is:
#
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
#
import unittest


class Solution:
    # @return a list of lists of integers

    def combine(self, n, k):
        res = []
        self.combineHelper(n, k, [], res)
        return res

    def combineHelper(self, n, k, path, res):
        if k == 0:
            res.append([i for i in path])
            return
        start = path[-1] + 1 if path else 1
        for i in range(start, n + 1):
            path.append(i)
            self.combineHelper(n, k - 1, path, res)
            path.pop()


class Test(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test(self):
        self.assertItemsEqual(self.s.combine(4, 2),
                              [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]])


if __name__ == '__main__':
    unittest.main()
