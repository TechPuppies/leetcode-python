# coding=utf-8
# AC Rate: 20.5%
# SOURCE URL: https://oj.leetcode.com/problems/spiral-matrix/
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
#
# For example,
# Given the following matrix:
#
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
#
#
# You should return [1,2,3,6,9,8,7,4,5].
#
#


class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        res = []
        if not matrix:
            return res

        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        flag = 0 # 0 left->right, 1 top->bottom, 2 right->left, 3 bottom->top
        # TODO edges break
        while left < right + 1 and top < bottom + 1:
            if flag == 0:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
                flag = 1
            elif flag == 1:
                for i in range(top, bottom+1):
                    res.append( matrix[i][right] )
                right -=1
                flag = 2
            elif flag == 2:
                for i in range(left, right + 1)[::-1]:
                    res.append( matrix[bottom][i] )
                bottom -= 1
                flag = 3
            elif flag == 3:
                for i in range(top, bottom+1)[::-1]:
                    res.append( matrix[i][left] )
                left += 1
                flag = 0
        return res

s = Solution()
print s.spiralOrder([
 [ 1]
])
    # top -> 1, right -> 1, bottom -> 1
