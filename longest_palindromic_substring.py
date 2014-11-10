# coding=utf-8
# AC Rate: 20.7%
# SOURCE URL: https://oj.leetcode.com/problems/longest-palindromic-substring/
#
# Given a string S, find the longest palindromic substring in S. You may assume
# that the maximum length of S is 1000, and there exists one unique longest
# palindromic substring.
#
import unittest


class Solution:
    # @return a string

    def oddPalindrome(self, s, k):
        i = 0
        while k - i >= 0 and k + i < len(s) and s[k - i] == s[k + i]:
            i += 1
        return s[k - i + 1:k + i]

    def evenPalindrome(self, s, k):
        i = 0
        while k - i >= 0 and k + 1 + i < len(s) and s[k - i] == s[k + 1 + i]:
            i += 1
        return s[k - i + 1:k + 1 + i]

    def longestPalindrome(self, s):
        best = ''
        for k in range(len(s)):
            odd = self.oddPalindrome(s, k)
            even = self.evenPalindrome(s, k)
            if len(odd) > len(best):
                best = odd
            if len(even) > len(best):
                best = even
        return best


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome('abcbaaddaa'), 'aaddaa')


if __name__ == '__main__':
    unittest.main()

# this is n ** 2
# there is O(n) alg
# http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
