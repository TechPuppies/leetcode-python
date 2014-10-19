
# coding=utf-8
# AC Rate: 21.1%
# SOURCE URL: https://oj.leetcode.com/problems/largest-rectangle-in-histogram/
#
#
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
#
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
#
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
#
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.
#
#


class Solution:
    # @param height, a list of integer
    # @return an integer

    def largestRectangleArea(self, height):
        stack, best = [], 0
        height.append(float('-inf'))
        for k in range(len(height)):
            if stack and height[stack[-1]] > height[k]:
                while stack and height[stack[-1]] > height[k]:
                    i = stack.pop()
                    if stack:
                        best = max(best, (k - stack[-1] - 1) * height[i])
                    else:
                        best = max(best, k * height[i])
            stack.append(k)
        return best

s = Solution()
print s.largestRectangleArea([2,1,5,6,2,3]) == 10
print s.largestRectangleArea([6,2,5,4,5]) == 12
print s.largestRectangleArea([7,7,7,7,4,5]) == 28
