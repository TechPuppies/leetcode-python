# coding=utf-8
# AC Rate: 20.5%
# SOURCE URL: https://oj.leetcode.com/problems/multiply-strings/
#
# Given two numbers represented as strings, return multiplication of the numbers as a string.
# Note: The numbers can be arbitrarily large and are non-negative.
#


class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        tmp, res = [], []
        for i in range(len(num2)):
            x = int(num2[len(num2) - 1 - i])
            current = []
            overflow = 0
            for j in range(len(num1)):
                y = int(num1[len(num1) - 1 - j])
                current.append((x * y + overflow) % 10)
                overflow = (x * y + overflow) / 10
            if overflow:
                current.append(overflow)
            tmp.append(current)
        # print tmp
        for k, i in enumerate(tmp):
            tmp[k] = [0] * k + tmp[k]

        overflow = 0
        for j in range(len(tmp[-1])):
            for i in tmp:
                if j < len(i):
                    overflow += i[j]
            res.append(str(overflow % 10))
            overflow /= 10
        if overflow:
            res.append(str(overflow))

        while res[-1] == '0' and len(res) > 1:
            res.pop()
        return ''.join(res[::-1])


s = Solution()
print s.multiply('140', '721')
def test(a, b):
    s = Solution()
    return s.multiply(a, b) == str(int(a) * int (b))
print test('128', '128')
print test('256', '256')
print test('128128128128128128128128256256256256256256256256', '128128128128128128128128128128128128128128128128128128128128256256256256256256256256256256256256')
