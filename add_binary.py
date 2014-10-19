# coding=utf-8
# AC Rate: 25.9%
# SOURCE URL: https://oj.leetcode.com/problems/add-binary/
#
#
# Given two binary strings, return their sum (also a binary string).
#
#
# For example,
# a = "11"
# b = "1"
# Return "100".
#
#
import unittest


class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        i, res, tmp = 0, [], 0
        while i < len(a) and i < len(b):
            c = int(a[-1-i]) + int(b[-1-i]) + tmp
            res.append(c % 2)
            i, tmp = i + 1, c / 2
        if i < len(b):
            a = b
        while i < len(a):
            c = int(a[-1-i]) + tmp
            res.append(c % 2)
            i, tmp = i + 1, c / 2
        if tmp:
            res.append(tmp)
        return ''.join([str(i) for i in res[::-1]])


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.addBinary('1010', '1011'), '10101')
        self.assertEqual(s.addBinary('1', '0'), '1')
        self.assertEqual(s.addBinary('11', '1'), '100')


if __name__ == '__main__':
    unittest.main()
