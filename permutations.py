# coding=utf-8
# AC Rate: 31.3%
# SOURCE URL: https://oj.leetcode.com/problems/permutations/
#
#
# Given a collection of numbers, return all possible permutations.
#
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
#
#
import unittest


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permutation(self, num):
        # dfs with recursion
        res = []
        self.helper(0, num, res)
        return res

    def helper(self, start, num, res):
        if start >= len(num):
            res.append(list(num))
        for i in range(start, len(num)):
            num[start], num[i] = num[i], num[start]
            self.helper(start + 1, num, res)
            num[start], num[i] = num[i], num[start]

    def permutation2(self, num):
        # dfs with stack
        # uses more space, I guess
        # compare to permutation1 which is recursion
        # probably the same space complexity
        res = []
        num.sort()
        stack = [(0, num)]
        while stack:
            start, num = stack.pop()
            if start >= len(num):
                res.insert(0, num)  # copy num
            for i in range(start, len(num)):
                num[i], num[start] = num[start], num[i]
                stack.append((start + 1, list(num)))
                num[i], num[start] = num[start], num[i]
        return res


class Test(unittest.TestCase):

    def test1(self):
        s = Solution()
        self.assertEqual(s.permutation([1, 2, 3]),
                         [[1, 2, 3], [1, 3, 2],
                          [2, 1, 3], [2, 3, 1],
                          [3, 2, 1], [3, 1, 2]])

    def test2(self):
        s = Solution()
        self.assertEqual(s.permutation2([1, 2, 3]),
                         [[1, 2, 3], [1, 3, 2],
                          [2, 1, 3], [2, 3, 1],
                          [3, 2, 1], [3, 1, 2]])

if __name__ == '__main__':
    unittest.main()
