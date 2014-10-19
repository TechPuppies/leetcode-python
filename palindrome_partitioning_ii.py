# coding=utf-8
# AC Rate: 18.0%
# SOURCE URL: https://oj.leetcode.com/problems/palindrome-partitioning-ii/
#
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
#
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
#
#
import collections
import unittest


class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # subproblem is cut from i then cutting s[i+1:]
        # before cut from i have to make sure s[:i] is palindrome
        self.dp = collections.defaultdict(int)
        self.calc_pal(s)
        return self.cutHelper(s, 0)

    def cutHelper(self, s, i):
        if i == len(s) - 1:
            return 0
        if i not in self.dp:
            if self.pal[i][-1]:
                self.dp[i] = 0
            else:
                n = float('inf')
                for j in range(i, len(s)):
                    if self.pal[i][j]:
                        n = min(n, self.cutHelper(s, j+1))
                self.dp[i] = 1 + n
        return self.dp[i]

    def calc_pal(self, s):
        self.pal = [[0] * len(s) for i in range(len(s))]
        for i in range(len(s)):
            self.pal[i][i] = 1
        for i in range(len(s) - 1):
            self.pal[i][i+1] = 1 if s[i] == s[i+1] else 0
        for k in range(2, len(s)):
            i, j = 0, k
            while i < len(s) and j < len(s):
                self.pal[i][j] = 1 if (self.pal[i+1][j-1] and s[i] == s[j]) else 0
                i += 1
                j += 1


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.minCut('cdd'), 1)
        self.assertEqual(s.minCut('aab'), 1)
        self.assertEqual(s.minCut('bccb'), 0)
        self.assertEqual(s.minCut('ccbbaabbccbb'), 1)
        self.assertEqual(s.minCut('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'), 1)


if  __name__ == '__main__':
    unittest.main()
