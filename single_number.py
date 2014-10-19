# coding=utf-8
# AC Rate: 45.8%
# SOURCE URL: https://oj.leetcode.com/problems/single-number/
#
# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
#


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for i in A:
            res ^= i
        return res

s = Solution()
print s.singleNumber([1,2,3,2,3,])
