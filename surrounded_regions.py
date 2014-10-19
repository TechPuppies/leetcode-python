# coding=utf-8
# AC Rate: 14.1%
# SOURCE URL: https://oj.leetcode.com/problems/surrounded-regions/
#
#
# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
#
# For example,
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
#
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
#


class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return

        blocks = set()
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'O':
                    blocks.add((i, j))

        while blocks:
            (x, y) = blocks.pop()
            self.bfs((x, y), board, blocks)


    def bfs(self, start, board, blocks):
        queue = [start]
        current = set([start])
        while queue:
            node = queue.pop()
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x += node[0]
                y += node[1]
                if (x, y) in current:
                    continue
                if x < 0 or y < 0 or x >= self.m or y >= self.n or \
                    ((x, y) not in blocks and board[x][y]) == 'O':
                    return
                if board[x][y] == 'O':
                    current.add((x, y))
                    blocks.remove((x, y))
                    queue.insert(0, (x, y))
        for x, y in current:
            board[x][y] = 'X'


import unittest

class Test(unittest.TestCase):

    def test(self):
        board = [
            ['X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X', 'X', 'O'],
            ['X', 'O', 'X', 'X', 'X', 'O'],
            ['X', 'X', 'X', 'X', 'X', 'O'],
        ]
        s = Solution()
        s.solve(board)
        self.assertEqual(board[1][1], 'X')
        self.assertEqual(board[1][2], 'X')
        self.assertEqual(board[2][2], 'X')
        self.assertEqual(board[2][4], 'X')
        self.assertEqual(board[3][1], 'X')
        self.assertEqual(board[4][1], 'X')
        self.assertEqual(board[3][5], 'O')
        self.assertEqual(board[4][5], 'O')
        self.assertEqual(board[5][5], 'O')


if __name__ == '__main__':
    unittest.main()
