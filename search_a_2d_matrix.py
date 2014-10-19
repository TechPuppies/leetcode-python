# coding=utf-8
# AC Rate: 31.2%
# SOURCE URL: https://oj.leetcode.com/problems/search-a-2d-matrix/
#
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
#
#
#
# For example,
#
# Consider the following matrix:
#
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
#
# Given target = 3, return true.
#
import unittest

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return None
        m, n = len(matrix), len(matrix[0])
        row = self.searchRow(matrix, 0, m - 1, target)
        if row == -1:
            return True
        return self.search(matrix, row, 0, n-1, target)

    def searchRow(self, matrix, s, e, target):
        if s == e:
            return s
        m = s + (e - s) / 2
        if matrix[m][-1] == target:
            return -1
        elif matrix[m][-1] > target:
            return self.searchRow(matrix, s, m, target)
        else:
            return self.searchRow(matrix, m + 1, e, target)

    def search(self, matrix, r, s, e, target):
        if e <= s:
            return matrix[r][s] == target
        m = s + (e - s) / 2
        if matrix[r][m] == target:
            return True
        elif matrix[r][m] > target:
            return self.search(matrix, r, s, m-1, target)
        else:
            return self.search(matrix, r, m+1, e, target)

class Test(unittest.TestCase):
    def test(self):
        matrix = [
              [1,   3,  5,  7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]
        ]
        s = Solution()
        self.assertTrue(s.searchMatrix(matrix, 1))
        self.assertTrue(s.searchMatrix(matrix, 3))
        self.assertTrue(s.searchMatrix(matrix, 5))
        self.assertTrue(s.searchMatrix(matrix, 7))
        self.assertTrue(s.searchMatrix(matrix, 10))
        self.assertTrue(s.searchMatrix(matrix, 11))
        self.assertTrue(s.searchMatrix(matrix, 16))
        self.assertTrue(s.searchMatrix(matrix, 20))
        self.assertTrue(s.searchMatrix(matrix, 23))
        self.assertTrue(s.searchMatrix(matrix, 30))
        self.assertTrue(s.searchMatrix(matrix, 34))
        self.assertTrue(s.searchMatrix(matrix, 50))
        self.assertFalse(s.searchMatrix(matrix, 0))
        self.assertFalse(s.searchMatrix(matrix, 4))
        self.assertFalse(s.searchMatrix(matrix, 6))
        self.assertFalse(s.searchMatrix(matrix, 9))
        self.assertFalse(s.searchMatrix(matrix, 12))
        self.assertFalse(s.searchMatrix(matrix, 14))
        self.assertFalse(s.searchMatrix(matrix, 13))
        self.assertFalse(s.searchMatrix(matrix, 21))
        self.assertFalse(s.searchMatrix(matrix, 24))
        self.assertFalse(s.searchMatrix(matrix, 31))
        self.assertFalse(s.searchMatrix(matrix, 37))
        self.assertFalse(s.searchMatrix(matrix, 52))
        self.assertFalse(s.searchMatrix([[]], 1))

if __name__ == '__main__':
    unittest.main()
