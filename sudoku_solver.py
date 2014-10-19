# coding=utf-8
# AC Rate: 20.8%
# SOURCE URL: https://oj.leetcode.com/problems/sudoku-solver/
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# Empty cells are indicated by the character '.'.
# You may assume that there will be only one unique solution.


class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        for i in range(9):
            board[i] = list(board[i])

        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))

        def dfs(board, empty, start):
            # print empty[start:]
            if start >= len(empty):
                return [''.join(i) for i in board]
            (i, j) = empty[start]
            for k in range(1, 10):
                k = str(k)
                if k not in board[i] \
                    and k not in [r[j] for r in board] \
                    and k not in board[(i/3)*3][(j/3)*3: (j/3)*3+3] \
                    and k not in board[(i/3)*3+1][(j/3)*3: (j/3)*3+3] \
                    and k not in board[(i/3)*3+2][(j/3)*3: (j/3)*3+3]:
                    board[i][j] = k
                    # if self.isValidSudoku(board):
                    res = dfs(board, empty, start + 1)
                    if res:
                        return res
                    board[i][j] = '.'
            return False

        return dfs(board, empty, 0)
    #
    # def isValidSudoku(self, board):
    #     lines_flip = [[False] * 9 for i in range(9)]
    #     rows_flip = [[False] * 9 for i in range(9)]
    #     block_flip = [[False] * 9 for i in range(9)]
    #     for r, line in enumerate(board):
    #         if not len(line) == 9:
    #             # base test
    #             return False
    #         for i, e in enumerate(line):
    #             # line
    #             if not e == '.':
    #                 flip_index = int(e) - 1
    #                 # if not self.ezCheck(r, flip_index, lines_flip):
    #                 #     return False
    #                 # if not self.ezCheck(i % 9, flip_index, rows_flip):
    #                 #     return False
    #                 if not self.ezCheck((r / 3) * 3 + (i / 3), flip_index, block_flip):
    #                     return False
    #     return True

    def ezCheck(self, r, i, flip):
        if flip[r][i] == True:
            return False
        else:
            flip[r][i] = True
        return True

s = Solution()
# print s.solveSudoku(
#     ['534678912',
#      '6..195348',
#      '.9834256.',
#      '859761423',
#      '4..8.3..1',
#      '7...2...6',
#      '.6153728.',
#      '...419..5',
#      '345286179']
# )
print s.solveSudoku(
    ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
)
# print s.solveSudoku(
#     ['53..7....',
#      '6..195...',
#      '.98....6.',
#      '8...6...3',
#      '4..8.3..1',
#      '7...2...6',
#      '.6....28.',
#      '...419..5',
#      '....8..79']
# )
