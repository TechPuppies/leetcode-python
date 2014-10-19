# coding=utf-8
# AC Rate: 18.9%
# SOURCE URL: https://oj.leetcode.com/problems/candy/
#
#
# There are N children standing in a line. Each child is assigned a rating value.
#
#
# You are giving candies to these children subjected to the following requirements:
#
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
#
#
# What is the minimum candies you must give?
#
#


class Solution:
    # @param ratings, a list of integer
    # @return an integer

    def candy(self, ratings):
        n = len(ratings)
        candy = [1] * n
        i = 1
        while i < n:
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
            i += 1

        i = n - 2
        while i >= 0:
            if ratings[i] > ratings[i + 1] and candy[i] <= candy[i + 1]:
                candy[i] = candy[i + 1] + 1
            i -= 1

        return sum(candy)


s = Solution()
print s.candy([]) == 0
print s.candy([1, 2, 2]) == 4
