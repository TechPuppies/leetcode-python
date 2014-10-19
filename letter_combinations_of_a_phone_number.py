# coding=utf-8
# AC Rate: 26.2%
# SOURCE URL: https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/
#
# Given a digit string, return all possible letter combinations that the number could represent.
#
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#
#


class Solution:
    # @return a list of strings, [s1, s2]
    mapping = {
        1: ['#'],
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits):
        result = []
        self.dfshelper(digits, '', result)
        return result

    def dfshelper(self, s, current, result):
        if not s:
            result.append(current)
            return

        for i in self.mapping[int(s[0])]:
            self.dfshelper(s[1:], current+i, result)

s = Solution()
print s.letterCombinations('96')
