# coding=utf-8
# AC Rate: 20.7%
# SOURCE URL: https://oj.leetcode.com/problems/longest-palindromic-substring/
#
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
#


class Solution:
    # @return a string
    def longestPalindrome(self, s):
        # O(n**2)
        best, match = 0, ''
        for k in range(len(s)):
            i = 0
            while k - i >= 0 and k + i < len(s) and s[k - i] == s[k + i]:
                i += 1
            if 2 * i - 1 > best:
                best = 2 * i - 1
                match = s[k-i+1:k+i]

            i = 0
            while k - i >= 0 and k + 1 + i < len(s) and s[k-i] == s[k+1+i]:
                i += 1
            if 2 * i > best:
                best = 2 * i
                match = s[k-i+1:k+i+1]
        return match

s = Solution()
print s.longestPalindrome('abcbaaddaa')


# this is n ** 2
# there is O(n) alg
# http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
