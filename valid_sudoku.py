# coding=utf-8
# AC Rate: 27.9%
# SOURCE URL: https://oj.leetcode.com/problems/valid-sudoku/
#
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
#
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
#
#


class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def ezCheck(self, r, i, flip):
        if flip[r][i] == True:
            return False
        else:
            flip[r][i] = True
        return True

    def isValidSudoku(self, board):
        lines_flip = [[False] * 9 for i in range(9)]
        rows_flip = [[False] * 9 for i in range(9)]
        block_flip = [[False] * 9 for i in range(9)]
        for r, line in enumerate(board):
            if not len(line) == 9:
                # base test
                return False
            for i, e in enumerate(line):
                # line
                if not e == '.':
                    flip_index = int(e) - 1
                    if not self.ezCheck(r, flip_index, lines_flip):
                        return False
                    if not self.ezCheck(i % 9, flip_index, rows_flip):
                        return False
                    if not self.ezCheck((r / 3) * 3 + (i / 3), flip_index, block_flip):
                        return False
        return True
