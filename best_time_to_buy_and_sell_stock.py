# coding=utf-8
# AC Rate: 31.0%
# SOURCE URL: https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# If you were only permitted to complete at most one transaction (ie, buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
#
import unittest


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        maxP, minB = 0, float('inf')
        for i in prices:
            maxP, minB = max(i - minB, maxP), min(i, minB)
        return maxP


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.maxProfit([2,1,2,0,1]), 1)


if __name__ == '__main__':
    unittest.main()
