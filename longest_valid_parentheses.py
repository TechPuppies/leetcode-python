# coding=utf-8
# AC Rate: 19.5%
# SOURCE URL: https://oj.leetcode.com/problems/longest-valid-parentheses/
#
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
#
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
#
#
import unittest

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        best, stack = 0, []
        for k, v in enumerate(')' + s):
            if v == ')' and stack and stack[-1][1] == '(':
                stack.pop()
                best = max(best, k - stack[-1][0])
            else:
                stack.append((k, v))
        return best


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.longestValidParentheses('))))())()()(()'), 4)
        self.assertEqual(s.longestValidParentheses('()(()'), 2)
        self.assertEqual(s.longestValidParentheses('(()'), 2)
        self.assertEqual(s.longestValidParentheses('(()()'), 4)
        self.assertEqual(s.longestValidParentheses('()()()()()()()()()()(((()(()()())))))'), 36)


if __name__ == '__main__':
    unittest.main()
