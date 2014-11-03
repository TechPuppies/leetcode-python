# coding=utf-8
# AC Rate: 13.7%
# SOURCE URL: https://oj.leetcode.com/problems/wildcard-matching/
#
# Implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") == False
# isMatch("aa","aa") == True
# isMatch("aaa","aa") == False
# isMatch("aa", "*") == True
# isMatch("aa", "a*") == True
# isMatch("ab", "?*") == True
# isMatch("aab", "c*a*b") == False
import unittest


class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean

    def isMatch(self, s, p):
        if s is None or p is None:
            return False
        ps, pp, match, astroid = 0, 0, 0, -1
        while ps < len(s):
            if pp < len(p) and (p[pp] == '?' or s[ps] == p[pp]):
                pp, ps = pp + 1, ps + 1
            elif pp < len(p) and p[pp] == '*':
                astroid, match, pp = pp, ps, pp + 1
            elif astroid >= 0:
                pp, match, ps  = astroid + 1, match + 1, match
            else:
                return False
        while pp < len(p) and p[pp] == '*':
            pp += 1
        return pp == len(p)


class Test(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test(self):
        self.assertFalse(self.s.isMatch("a", "aa"))
        self.assertFalse(self.s.isMatch("aa", "a"))
        self.assertEqual(self.s.isMatch("aa", "aa"), True)
        self.assertEqual(self.s.isMatch("aaa", "aa"), False)
        self.assertEqual(self.s.isMatch("aa", "*"), True)
        self.assertEqual(self.s.isMatch("aa", "a*"), True)
        self.assertEqual(self.s.isMatch("ab", "?*"), True)
        self.assertEqual(self.s.isMatch("aab", "c*a*b"), False)
        self.assertEqual(self.s.isMatch("aab", "c*a*b"), False)
        self.assertEqual(self.s.isMatch("", ""), True)
        self.assertEqual(self.s.isMatch(None, None), False)
        self.assertEqual(
            self.s.isMatch(
                "aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba",
                "a*******b"),
            False)
        self.assertEqual(
            self.s.isMatch(
                "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbba" + \
                "bbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb",
                "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"),
            True)
        self.assertEqual(
            self.s.isMatch(
                'abbbabaaabbabbabbabaabbbaabaaaabbbabaaabbbbbaaababbb',
                '**a*b*aa***b***bbb*ba*a'),
            False)


if __name__ == '__main__':
    unittest.main()
