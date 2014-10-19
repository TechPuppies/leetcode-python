# coding=utf-8
# AC Rate: 16.3%
# SOURCE URL: https://oj.leetcode.com/problems/divide-two-integers/
#
#
# Divide two integers without using multiplication, division and mod operator.
#
#


class Solution:
    # @return an integer
    def divide(self, x, y):
        neg = ((x>=0) ^ (y>=0))
        x, y = abs(x), abs(y)
        res = 0
        while x >= y:
            k = 0
            while y << k < x and y << k + 1 <= x:
                k += 1

            # print x, y, k
            res += 1 << k
            x -= y << k
        return -res if neg else res


s = Solution()
print s.divide(1,-1) == -1
print s.divide(4,2) == 2
print s.divide(9,2) == 9 / 2
print s.divide(321329,3212) == 321329 / 3212
print s.divide(5382190382901, 13281903) == 5382190382901 / 13281903
