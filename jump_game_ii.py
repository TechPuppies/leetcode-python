# coding=utf-8
# AC Rate: 24.6%
# SOURCE URL: https://oj.leetcode.com/problems/jump-game-ii/
#
#
# Given an array of non-negative integers, you are initially positioned
# at the first index of the array.
#
#
# Each element in the array represents your maximum jump length at that
# position.
#
#
# Your goal is to reach the last index in the minimum number of jumps.
#
#
# For example:
# Given array A = [2,3,1,1,4]
#
#
# The minimum number of jumps to reach the last index is 2.
# (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#
#
import unittest

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        ret, last, curr = 0, 0, 0
        for i in range(len(A)):
            if i > last:  # if not last one and can't go further
                if (curr == last) and (last < len(A)-1):
                    return -1   # never reach the last one
                last, ret = curr, ret + 1
            curr = max(curr, i+A[i])
        return ret


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.jump([0]), 0)
        self.assertEqual(s.jump([2, 1]), 1)
        self.assertEqual(s.jump([1, 2, 0, 1]), 2)
        self.assertEqual(s.jump([2, 3, 1, 1, 4]), 2)
        self.assertEqual(s.jump([1 for i in range(250000)]), 249999)

if __name__ == '__main__':
    unittest.main()
