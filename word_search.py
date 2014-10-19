# coding=utf-8
# AC Rate: 19.9%
# SOURCE URL: https://oj.leetcode.com/problems/word-search/
#
#
# Given a 2D board and a word, find if the word exists in the grid.
#
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
#
# For example,
# Given board =
#
# [
#   ["ABCE"],
#   ["SFCS"],
#   ["ADEE"]
# ]
#
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
#
#


class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean

    def neibough(self, ii, jj, board):
        if ii + 1 < len(board):
            yield((ii+1, jj))
        if ii - 1 >= 0:
            yield((ii-1, jj))
        if jj + 1 < len(board[0]):
            yield((ii, jj+1))
        if jj - 1 >= 0:
            yield((ii, jj-1))

    def exist(self, board, word):
        for i in range(len(board)):
            board[i] = list(board[i])

        stack = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    stack.append(([(i, j)], 1))

        while stack:
            chain, length = stack.pop()
            # end
            if length == len(word):
                # it is a finish point
                return True
            target = word[length]
            chain_tail = chain[-1]
            for (ii, jj) in self.neibough(chain_tail[0], chain_tail[1], board):
                if board[ii][jj] == target and (ii, jj) not in chain:
                    stack.append((chain+[(ii, jj)], length + 1))
        return False

s = Solution()
print s.exist(
    [
      "ABCE",
      "SFCS",
      "ADEE"
    ], "ABCES"
)
