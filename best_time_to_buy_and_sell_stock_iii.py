# coding=utf-8
# AC Rate: 22.2%
# SOURCE URL: https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
#
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#


class Solution:
    # @param prices, a list of integer
    # @return an integer

    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        for k in range(len(prices) - 1):
            prices[k] = prices[k + 1] - prices[k]
        # prices[-1] = 0
        # print prices[:-1]

        best = 0
        current = 0
        histroy_best = [0] * (len(prices) - 1)
        for k, i in enumerate(prices[:-1]):
            # print best, second
            current += i
            if current < 0:
                current = 0
            best = max(best, current)
            histroy_best[k] = best

        best = 0
        current = 0
        final_best = max(histroy_best)
        for k, i in enumerate(prices[1:-1][::-1]):
            current += i
            if current < 0:
                current = 0
            best = max(best, current)
            final_best = max(final_best, best + histroy_best[-k - 2])
        # return best + second
        return final_best

s = Solution()
prices = []
print s.maxProfit(prices)
