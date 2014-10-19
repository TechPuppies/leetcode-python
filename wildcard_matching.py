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
#
#


class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        self.s = s
        self.p = p
        return self.helper(0, 0)

    def helper(self, ps, pp):
        if self.s is None or self.p is None:
            return False
        if ps >= len(self.s) or pp >= len(self.p):
            if pp >= len(self.p) and ps >= len(self.s):
                return True
            else:
                return False

        if self.s[ps] == self.p[pp] or self.p[pp] == '?':
            return self.helper(ps+1, pp+1)
        elif self.p[pp] == '*':
            while pp < len(self.p) and self.p[pp] == '*':
                pp += 1
                if pp == len(self.p):
                    return True
            return self.helper(ps, pp) or self.helper(ps+1, pp-1)
        return False


s = Solution()
print s.isMatch("a","aa") == False
print s.isMatch("aa","a") == False
print s.isMatch("aa","aa") == True
print s.isMatch("aaa","aa") == False
print s.isMatch("aa", "*") == True
print s.isMatch("aa", "a*") == True
print s.isMatch("ab", "?*") == True
print s.isMatch("aab", "c*a*b") == False
print s.isMatch("aab", "c*a*b") == False
print s.isMatch("", "") == True
print s.isMatch(None, None) == False
print s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b") == False
print s.isMatch("abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb",
    "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**") == True
print s.isMatch('abbbabaaabbabbabbabaabbbaabaaaabbbabaaabbbbbaaababbb', '**a*b*aa***b***bbb*ba*a') == False
