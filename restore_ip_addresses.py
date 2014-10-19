# coding=utf-8
# AC Rate: 20.5%
# SOURCE URL: https://oj.leetcode.com/problems/restore-ip-addresses/
#
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#
#


class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        res = []
        stack = [([], s)]
        while stack:
            comb, s = stack.pop()
            lens = len(s)
            lenc = len(comb)
            if not s:
                if lenc == 4:
                    res.append('.'.join(comb))
                continue
            # children
            if lens >= 1 and lens + 3 * lenc <= 10 :
                # can be 0
                stack.append((comb+[s[:1]], s[1:]))
            if lens >= 2 and lens + 3 * lenc <= 11 and s[:2][0] != '0':
                # cannot starts with 0
                stack.append((comb+[s[:2]], s[2:]))
            if lens >= 3 and lens + 3 * lenc <= 12 and int(s[:3]) <= 255 and s[:3][0] != '0':
                # cannot starts with 0
                stack.append((comb+[s[:3]], s[3:]))
        return res


s = Solution()
print s.restoreIpAddresses('25525511135')
print s.restoreIpAddresses('010010')
