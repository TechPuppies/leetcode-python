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
        self.prepareT(T)
        start, end, found = 0, len(S) - 1, False
        best_start, best_end = start, end
        for k in range(len(S)):
            if S[k] in self.dic:
                self.dic[S[k]] -= 1
                if self.dic[S[k]] == 0:
                    self.counter -= 1
                    if self.counter == 0:
                        end = k
                        found = True
                        # start move
                        while start < end:
                            if S[start] in self.dic:
                                self.dic[S[start]] += 1
                                if self.dic[S[start]] > 0:
                                    self.counter += 1
                            start += 1
                            if self.counter > 0:
                                break


        if not found:
            return ''
        return S[max(0, start-1):end+1]


    def prepareT(self, T):
        self.dic = {}
        for i in T:
            if i not in self.dic:
                self.dic[i] = 1
            else:
                self.dic[i] += 1
        self.counter = len(self.dic.keys())


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.minWindow('ADOBECODEBANC', 'BANC'), 'BANC')
        self.assertEqual(s.minWindow('A', 'A'), 'A')
        self.assertEqual(s.minWindow('A', 'AA'), '')
        self.assertEqual(s.minWindow('Ab', 'A'), 'A')


if __name__ == '__main__':
    unittest.main()
