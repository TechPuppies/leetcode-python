# coding=utf-8
# AC Rate: 16.9%
# https://oj.leetcode.com/problems/3sum/

# Given an array S of n integers,
# are there elements a, b, c in S such that a + b
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤
# The solution set must not contain duplicate triplets.
#     For example, given array S = {-1 0 1 2 -1 -4},
#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)
import unittest


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]

    def twoSum(self, num, target, start):
        dic, res, already = {}, [], set()
        for i in range(start, len(num)):
            if target - num[i] in dic and num[i] not in already:
                already.add(num[i])
                res.append([num[dic[target - num[i]]], num[i]])
            dic[num[i]] = i
        return res

    def threeSum(self, num):
        res = []
        num.sort()
        for k, v in enumerate(num):
            if k == 0 or num[k] != num[k - 1]:
                t = self.twoSum(num, 0 - v, k + 1)
                for n in t:
                    res.append([v, n[0], n[1]])
        return res


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.threeSum([0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(s.threeSum([-1, 0, 0, 3, 1, 2, -1, -4]),
                         [[-4, 1, 3], [-1, 0, 1], [-1, -1, 2]])


if __name__ == '__main__':
    unittest.main()
