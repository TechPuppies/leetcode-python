# coding=utf-8
# AC Rate: 16.4%
# SOURCE URL: https://oj.leetcode.com/problems/word-break-ii/
#
#
# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
#
#
# Return all such possible sentences.
#
#
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
#
# A solution is ["cats and dog", "cat sand dog"].
#
#
#


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings

    def collect(self, t, s, start, current, res):
        for j in t[start]:
            current.append(s[start: j])
            if j == len(s):
                res.append(' '.join(current))
            else:
                self.collect(t, s, j, current, res)
            current.pop()


    def wordBreak(self, s, d):
        p = [False] * (len(s) + 1)
        t = [[] for i in range(len(s) + 1)]
        p[0] = True
        d = set(d)
        for i in range(len(s)):
            if not p[i]:
                continue

            for j in d:
                if j == s[i:i+len(j)]:
                    p[i+len(j)] = True
                    t[i].append(i+len(j))
        res = []
        if p[-1]:
            self.collect(t, s, 0, [], res)
        return res


if __name__ == '__main__':
    s = Solution()
    # print s.wordBreak("aaaaaaa", ["aaaa","aa","a"])
    # print s.wordBreak('leetcode', ['leet', 'lee', 'code', 'tcode'])
    # print
    print s.wordBreak("a", ["a"])
    # print s.wordBreak('a', [])
    # print s.wordBreak('aaaaaaa', ["aaaa","aaa"])
    # print s.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"])
    # print s.wordBreak(
    #     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    #     ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"])
