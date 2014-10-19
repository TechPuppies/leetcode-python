# coding=utf-8
# AC Rate: 16.0%
# SOURCE URL: https://oj.leetcode.com/problems/decode-ways/
#
#
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
#
# For example,
# Given encoded message "12",
# it could be decoded as "AB" (1 2) or "L" (12).
#
#
# The number of ways decoding "12" is 2.
#
#


class Solution:
    # @param s, a string
    # @return an integer
    def base(self, s):
        res = 0
        if len(s) == 1:
            if int(s) > 0:
                res += 1
        elif len(s) == 2:
            if int(s) > 26:
                if s[1] != '0':
                    res += 1
            else:
                if s[0] != '0':
                    res += 1
                    if s[1] != '0':
                        res +=1
        return res

    def numDecodings(self, s):
        self.dp = {}
        return self.helper(s)

    def helper(self, s):
        if len(s) <= 2:
            return self.base(s)

        if s not in self.dp:
            count = 0
            stack = [s]
            while stack:
                s = stack.pop()
                if len(s) == 0:
                    count += 1
                    continue
                if len(s) > 0:
                    if s[0] != '0':
                        if int(s[:1]) >= 1:
                            count += self.helper(s[1:])
                        if len(s) > 1:
                            if int(s[:2]) <= 26:
                                count +=  self.helper(s[2:])
            self.dp[s] = count
        return self.dp[s]


s = Solution()
print s.numDecodings('4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948') == 589824
print s.numDecodings('10') == 1
print s.numDecodings('101') == 1
print s.numDecodings('0') == 0
print s.numDecodings('012') == 0
