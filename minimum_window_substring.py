# coding=utf-8
# AC Rate: 17.9%
# SOURCE URL: https://oj.leetcode.com/problems/minimum-window-substring/
#
#
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
#
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
#
#
# Minimum window is "BANC".
#
#
# Note:
# If there is no such window in S that covers all characters in T, return the emtpy string "".
#
#
# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
#
#
import unittest


class Solution:
    # @return a string

    def minWindow(self, S, T):
        self.dic, self.counter = self.prepareT(T)
        start, end, best, res = -1, 0, len(S), ''
        while end is not None:
            end = self.moveEnd(S, end)
            start = self.moveStart(S, start)
            if end and end - start <= best:
                best = end - start
                res = S[start:end]
        return res

    def moveStart(self, S, start):
        start += 1
        while start < len(S):
            if S[start] in self.dic:
                self.dic[S[start]] += 1
                if self.dic[S[start]] > 0:
                    self.counter += 1
                    return start
            start += 1

    def moveEnd(self, S, end):
        while end < len(S):
            if S[end] in self.dic:
                self.dic[S[end]] -= 1
                if self.dic[S[end]] == 0:
                    self.counter -= 1
                    if self.counter == 0:
                        return end + 1
            end += 1
        return None

    def prepareT(self, T):
        dic = {}
        for i in T:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        return dic, len(dic)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.minWindow('ADOBECODEBANC', 'BANC'), 'BANC')
        self.assertEqual(s.minWindow('A', 'A'), 'A')
        self.assertEqual(s.minWindow('A', 'AA'), '')
        self.assertEqual(s.minWindow('Ab', 'A'), 'A')
        self.assertEqual(s.minWindow('ab', 'b'), 'b')


if __name__ == '__main__':
    unittest.main()
