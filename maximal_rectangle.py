# coding=utf-8
# AC Rate: 21.6%
# SOURCE URL: https://oj.leetcode.com/problems/maximal-rectangle/
#
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
#
#


class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        for i in range(len(matrix)):
            matrix[i] = [int(j) for j in list(matrix[i])]


        tab = [[None] * len(matrix[0]) for i in range(len(matrix))]
        w, h = 0, 0
        # todo initial dp
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    if row-1 >= 0:
                        h = tab[row-1][col][1] + 1
                    else:
                        h = 1
                    if col-1 >= 0:
                        w = tab[row][col-1][0] + 1
                    else:
                        w = 1
                    tab[row][col] = (w, h)
                else:
                    tab[row][col] = (0, 0)

        best = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (tab[row][col][0] * tab[row][col][1]) > best:
                    minW = float('inf')
                    for k in range(tab[row][col][1]):
                        minW = min(minW, tab[row-k][col][0])
                        rectangle = (k + 1) * minW
                        best = max(best, rectangle)
        return best


s = Solution()
print s.maximalRectangle(
    [
        "01101",
        "11010",
        "11110",
        "11010",
        "11111",
        "00000"
    ]
)
