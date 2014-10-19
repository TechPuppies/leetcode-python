# coding=utf-8
# AC Rate: 22.3%
# SOURCE URL: https://oj.leetcode.com/problems/sqrtx/
#
# Implement int sqrt(int x).
# Compute and return the square root of x.
#


class Solution:
    # @param x, an integer
    # @return an integer

    def helper(self, x, start, end):
        if start >= end:
            return end
        mid = start + (end - start) / 2
        if mid ** 2 == x:
            return mid
        elif mid ** 2 > x:
            if (mid - 1) ** 2 <= x:
                return mid - 1
            return self.helper(x, start, mid - 1)
        else:
            if (mid + 1) ** 2 > x:
                return mid
            return self.helper(x, mid + 1, end)

    def sqrt(self, x):
        if x <= 1:
            return x
        return self.helper(x, 0, x / 2)

if __name__ == '__main__':
    s = Solution()
    print s.sqrt(10)  # 2147395599

