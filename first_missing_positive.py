# coding=utf-8
# AC Rate: 22.5%
# SOURCE URL: https://oj.leetcode.com/problems/first-missing-positive/
#
#
# Given an unsorted integer array, find the first missing positive integer.
#
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
#
# Your algorithm should run in O(n) time and uses constant space.
#
#


class Solution:
    # @param A, a list of integers
    # @return an integer

    def firstMissingPositive(self, A):
        if not A:
            return 1
        for k, i in enumerate(A):
            while i - 1 < len(A) and i - 1 >= 0:
                tmp = A[i - 1]
                A[i - 1] = i
                if i - 1 > k and not i == tmp:
                    A[k] = tmp
                    i = tmp
                else:
                    break
        for k, i in enumerate(A):
            if not k == i - 1:
                return k + 1
        return len(A) + 1

s = Solution()
print s.firstMissingPositive([1])
# print s.firstMissingPositive([3,4, -1, 1])
