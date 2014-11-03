# coding=utf-8
# AC Rate: 33.9%
# SOURCE URL: https://oj.leetcode.com/problems/climbing-stairs/
#
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
import unittest


class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        """
        this should be able to use dp
        """
        a, b = 1, 1
        for i in range(n-1):
            a, b = a+b, a
        return a


class Test(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test(self):
        self.assertEqual(self.s.climbStairs(2), 2)
        self.assertEqual(self.s.climbStairs(3), 3)
        self.assertEqual(self.s.climbStairs(4), 5)

if __name__ == '__main__':
    unittest.main()
