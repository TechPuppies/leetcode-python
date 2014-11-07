# coding=utf-8
# AC Rate: 31.1%
# SOURCE URL: https://oj.leetcode.com/problems/container-with-most-water/
#
# Given n non-negative integers a1, a2, ..., an, where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
# forms a container, such that the container contains the most water.
#
# Note: You may not slant the container.
#
#
import unittest


class Solution:
    # @return an integer

    def maxArea(self, height):
        """
        i = 0, j = n - 1. the width always getting shorter
        the height will be min(height[i], height[j])
        """
        i, j, maxArea = 0, len(height) - 1, 0
        while i < j:
            maxArea = max(min(height[i], height[j]) * (j - i), maxArea)
            i, j = (i, j - 1) if height[i] > height[j] else (i + 1, j)
        return maxArea


class Test(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test(self):
        self.assertEqual(self.s.maxArea([3, 2, 1, 2, 3]), 12)


if __name__ == '__main__':
    unittest.main()
