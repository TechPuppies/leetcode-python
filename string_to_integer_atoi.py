# coding=utf-8
# AC Rate: 14.6%
# SOURCE URL: https://oj.leetcode.com/problems/string-to-integer-atoi/
#
# Implement atoi to convert a string to an integer.
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
#
# Notes:
# It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
# spoilers alert... click to show requirements for atoi.
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
#
#
#


class Solution:
    # @return an integer
    def listToInteger(self, resA, neg):
        res = 0
        for i in resA:
            res = res * 10 + i
            if not neg and res > 2147483647:
                return 2147483647
            if neg and res > 2147483648:
                return -2147483648
        return res if not neg else -res

    def atoi(self, ss):
        num = set(['0','1','2','3','4','5','6','7','8','9'])
        start, neg = False, False
        resA = []
        for cc in ss:
            if cc not in ['+', '-', '.', ' '] and cc not in num:
                break
            if cc in num:
                start = True
            if start:
                if cc in num:
                    resA.append(int(cc))
                else:
                    break
            if not start and cc in ['+', '-']:
                neg = cc == '-'
                start = True
        return self.listToInteger(resA, neg)

s = Solution()
print s.atoi('+-20') == 0
print s.atoi('  -0012a42') == -12
print s.atoi('    010') == 10
print s.atoi('11228552307.0') == 2147483647
print s.atoi('111.11') == 111
print s.atoi('b11228552307') == 0
print s.atoi('1a389201839.999') == 0
print s.atoi('-1111') == -1111
print s.atoi('-2147483649') == -2147483648
print s.atoi('2147483648') == 2147483647
