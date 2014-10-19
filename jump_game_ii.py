# coding=utf-8
# AC Rate: 24.6%
# SOURCE URL: https://oj.leetcode.com/problems/jump-game-ii/
#
#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
#
# Each element in the array represents your maximum jump length at that position.
#
#
# Your goal is to reach the last index in the minimum number of jumps.
#
#
# For example:
# Given array A = [2,3,1,1,4]
#
#
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#
#
import unittest


class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # use inf present not possible
        jumpSteps = [float('inf')] * len(A)
        # target to target == 0
        jumpSteps[-1] = 0
        for i in xrange(len(A) - 2, -1, -1):
            jumpSteps[i] = 1 + min([jumpSteps[i + j] for j in xrange(1, A[i] + 1)])
        return jumpSteps[0]


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.jump([2,3,1,1,4]), 2)
        self.assertEqual(s.jump([1 for i in range(250000)]), 249999)

if __name__ == '__main__':
    unittest.main()
