# coding=utf-8
# AC Rate: 22.3%
# SOURCE URL:
# https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Given a string, find the length of the longest substring without repeating
# characters. For example, the longest substring without repeating letters
# for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest
# substring is "b", with the length of 1.
#
import unittest


class Solution:
    # @return an integer

    def lengthOfLongestSubstringAgain(self, s):
        # dp[i] is the longest ends with s[j]
        # using set not a list to count
        # good enough, but more intuitive
        start, occur, best = 0, set([s[0]]) , 0
        for k in range(1, len(s)):
            if s[k] in occur:
                for i in range(start, k):
                    if s[i] == s[k]:
                        break
                    occur.remove(s[i])
                start = i + 1
            else:
                occur.add(s[k])
            best = max(best, k - start + 1)
        return best


    def lengthOfLongestSubstring(self, s):
        i, j, maximum = 0, 0, 0
        latest = [False] * 256
        while i < len(s):
            if latest[ord(s[i])]:
                maximum = max(maximum, i - j)
                while not s[j] == s[i]:
                    latest[ord(s[j])] = False
                    j += 1
                j+=1
            else:
                latest[ord(s[i])] = True
            i += 1
        maximum = max(maximum, len(s) - j)
        return maximum


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstringAgain('bbb'), 1)
        self.assertEqual( s.lengthOfLongestSubstring('abcabcbb'), 3)
        self.assertEqual( s.lengthOfLongestSubstring('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco'), 12)
        self.assertEqual( s.lengthOfLongestSubstringAgain('qopubjguxhxdipfzwswybgfylqvjzhar'), 12)
        self.assertEqual( s.lengthOfLongestSubstringAgain('hnwnkuewhsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcac'), 12)


if __name__ == '__main__':
    unittest.main()
