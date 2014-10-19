# coding=utf-8
# AC Rate: 27.2%
# SOURCE URL: https://oj.leetcode.com/problems/count-and-say/
#
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
#
# Given an integer n, generate the nth sequence.
#
#
# Note: The sequence of integers will be represented as a string.
#
#
#
import unittest


class Solution:
    # @return a string

    def countAndSay(self, n):
        if n < 1:
            raise ValueError
        if n == 1:
            return '1'
        prev = self.countAndSay(n - 1) + ' '
        say, count, tmp = [], 1, prev[0]
        for i in prev[1:]:
            if i == tmp:
                count += 1
            else:
                say.append(str(count))
                say.append(tmp)
                tmp, count = i, 1
        return ''.join(say)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.countAndSay(2), '11')
        self.assertEqual(s.countAndSay(3), '21')
        self.assertEqual(s.countAndSay(4), '1211')
        self.assertEqual(s.countAndSay(5), '111221')


if __name__ == '__main__':
    unittest.main()
