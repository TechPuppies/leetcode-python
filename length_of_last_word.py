# coding=utf-8
# AC Rate: 29.3%
# SOURCE URL: https://oj.leetcode.com/problems/length-of-last-word/
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.
# Note: A word is defined as a character sequence consists of non-space
# characters only.
#
# For example,
# Given s = "Hello World",
# return 5.
#
#
import unittest


class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        for i in range(1, len(s) + 1):
            if s[-i] == ' ':
                return i - 1
        return len(s)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.lengthOfLastWord('Hello World'), 5)


if __name__ == '__main__':
    unittest.main()
