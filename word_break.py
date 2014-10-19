# coding=utf-8
# AC Rate: 21.0%
# SOURCE URL: https://oj.leetcode.com/problems/word-break/
#
#
# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
#
# Return true because "leetcode" can be segmented as "leet code".
#
#


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean

    def wordBreak(self, s, d):
        if not s:
            return False
        t = [False] * (len(s) + 1)
        t[0] = True
        for i in range(len(s)):
            if (not t[i]): continue
            for j in d:
                if j == s[i:i+len(j)]:
                    t[i+len(j)] = True
                continue
        return t[-1]

if __name__ == '__main__':
    s = Solution()
    print s.wordBreak('leetcode', ['leet', 'lee', 'code'])
    print s.wordBreak('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
