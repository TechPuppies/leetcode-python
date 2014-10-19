# coding=utf-8
# AC Rate: 27.2%
# SOURCE URL: https://oj.leetcode.com/problems/jump-game/
#
#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
#
# Each element in the array represents your maximum jump length at that position.
#
#
# Determine if you are able to reach the last index.
#
#
# For example:
# A = [2,3,1,1,4], return true.
#
#
# A = [3,2,1,0,4], return false.
# length = 5, canJum[3] = if(A[3] >= length-1-i)
#
import unittest


class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        end = len(A)
        canJump = [0] * len(A)
        canJump[-1] = 1
        for i in xrange(len(A)-2, -1, -1):
            for j in xrange(1, A[i] + 1):
                if canJump[i + j] == 1:
                    canJump[i] = 1
                    break
        return canJump[0] > 0


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertTrue(s.canJump([2,3,1,1,4]))
        self.assertFalse(s.canJump([3,2,1,0,4]))
        self.assertTrue(s.canJump(range(25000)[::-1]+range(25000)))


if __name__ == '__main__':
    unittest.main()
