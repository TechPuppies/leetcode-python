# coding=utf-8
# AC Rate: 31.4%
# SOURCE URL: https://oj.leetcode.com/problems/generate-parentheses/
#
#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
# For example, given n = 3, a solution set is:
#
#
# "((()))", "(()())", "(())()", "()(())", "()()()"
#
#


class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        # depth first search
        res = []
        stack = [('(', 1, 0)]
        while stack:
            s, l, r = stack.pop()
            if l < n:
                stack.append((s+'(', l+1, r))
            if r < l:
                stack.append((s+')', l, r+1))
            if r == n:
                res.append(s)
        return res

s = Solution()
print s.generateParenthesis(4)
