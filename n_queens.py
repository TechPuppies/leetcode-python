# coding=utf-8
# AC Rate: 25.9%
# SOURCE URL: https://oj.leetcode.com/problems/n-queens/
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#
#
import unittest


class Solution:
    # @return a list of lists of string

    def dfsHelper(self, col, res):
        if col >= self.n:
            res.append(self.print_board())
            return
        for i in range(self.n):
            if not self.is_attack(col, i):
                self.board[i][col] = 1
                self.dfsHelper(col + 1, res)
                self.board[i][col] = 0

    def is_attack(self, col, i):
        for col_ahead in range(col):
            if self.board[i][col_ahead] == 1:
                return True
            col_diff = col - col_ahead
            if i-col_diff >= 0 and self.board[i-col_diff][col_ahead] == 1:
                return True
            if i+col_diff < self.n and self.board[i+col_diff][col_ahead] == 1:
                return True
        return False

    def print_board(self):
        res = []
        for row in self.board:
            res.append(''.join(['Q' if b else '.' for b in row]))
        return res

    def solveNQueens(self, n):
        self.n = n
        self.board = [[0] * n for i in range(n)]
        res = []
        self.dfsHelper(0, res)
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.solveNQueens(4),
                         [['..Q.', 'Q...', '...Q', '.Q..'],
                          ['.Q..', '...Q', 'Q...', '..Q.']])


if __name__ == '__main__':
    unittest.main()
