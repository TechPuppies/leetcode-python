# coding=utf-8
# AC Rate: 24.8%
# SOURCE URL: https://oj.leetcode.com/problems/distinct-subsequences/
#
#
# Given a string S and a string T, count the number of distinct subsequences of T in S.
#
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
#
# Here is an example:
# S = "rabbbit", T = "rabbit"
#
#
# Return 3.
#
#
# T.substr(1...i) in S(1...j)


class Solution:
    # @return an integer

    def numDistinct(self, S, T):
        p = [[0] * (len(S) + 1) for i in range(len(T) + 1)]
        for k in range(len(p[0])):
            p[0][k] = 1

        for j in range(1, len(S) + 1):
            for i in range(1, len(T) + 1):
                if not S[j - 1] == T[i - 1]:
                    p[i][j] = p[i][j - 1]
                else:
                    p[i][j] = p[i][j - 1] + p[i - 1][j - 1]

        return p[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    S, T = "rabbbit", "rabbit"
    print solution.numDistinct(S, T)
    S, T = "acaaaacbcbcccabbabccc", "caa"
    print solution.numDistinct(S, T)
    S, T = "anacondastreetracecar", "contra"
    print solution.numDistinct(S, T)
    S, T = "bccbcdcabadabddbccaddcbabbaaacdba", "bccbbdc"
    print solution.numDistinct(S, T)
