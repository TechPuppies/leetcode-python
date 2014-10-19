# coding=utf-8
# AC Rate: 24.5%
# SOURCE URL: https://oj.leetcode.com/problems/combination-sum-ii/
#
#
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.
#
#
#
# For example, given candidate set 10,1,2,7,6,1,5 and target 8,
# A solution set is:
# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]
#
#

import copy


class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers

    def helper(self, candidates, target, start):
        # print target
        res = []

        if target == 0:
            return [[], ]

        i = start
        while i < len(candidates):
            if target >= candidates[i]:
                for j in self.helper(candidates, target - candidates[i], i + 1):
                    j.append(candidates[i])
                    res.append(j)
                    while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                        i += 1
            i += 1
        return res

    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.helper(candidates[::-1], target, 0)

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    # print s.combinationSum2([14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12,
    # 31, 9, 9, 12, 34, 16, 25, 32, 8, 7, 30, 12, 33, 20, 21, 29, 24, 17, 27,
    # 34, 11, 17, 30, 6, 32, 21, 27, 17, 16, 8, 24, 12, 12, 28, 11, 33, 10,
    # 32, 22, 13, 34, 18, 12], 27)
