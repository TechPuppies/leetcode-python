# coding=utf-8
# AC Rate: 18.0%
# SOURCE URL: https://oj.leetcode.com/problems/substring-with-concatenation-of-all-words/
#
#
# You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.
#
#
# For example, given:
# S: "barfoothefoobarman"
# L: ["foo", "bar"]
#
#
# You should return the indices: [0,9].
# (order does not matter).
#
#
import unittest


class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        ll, w = len(L), len(L[0])
        t, hr = ll * w, sum([hash(i) for i in L])
        h = [hash(S[i:i+w]) * (S[i:i+w] in L) for i in range(len(S) - w + 1)]
        return [i for i in xrange(len(S)-t+1) if sum(h[i:i+t:w]) == hr]



class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.findSubstring('barfoothefoobarman', ['foo', 'bar']), [0, 9])

if __name__ == '__main__':
    unittest.main()
