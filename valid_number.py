# coding=utf-8
# AC Rate: 11.0%
# SOURCE URL: https://oj.leetcode.com/problems/valid-number/
#
# Validate if a given string is numeric.
#
# Some examples:
# "0" => true
# "   0.1  " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
#
# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
#
#


class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        try:
            float(s)
            return True
        except:
            return False

s = Solution()
print s.isNumber('0e') == False,
print s.isNumber('+0') == True,
print s.isNumber('0') == True,
print s.isNumber('0.1') == True,
print s.isNumber('abc') == False,
print s.isNumber('1 a') == False,
print s.isNumber('2e10') == True,
print s.isNumber('6e6.5') == False,
print s.isNumber('6.5e6') == True,
print s.isNumber('6.5e6.5') == False,
print s.isNumber('e') == False,
print s.isNumber('.1') == True,
print s.isNumber('.') == False,
print s.isNumber('3.') == True,
print s.isNumber('-3.') == True,
print s.isNumber('e9') == False,
print s.isNumber('46.e9') == True,
print s.isNumber('.e1') == True,
