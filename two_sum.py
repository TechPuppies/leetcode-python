# coding=utf-8
# AC Rate: 18.5%
# SOURCE URL: https://oj.leetcode.com/problems/two-sum/
#
# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
#
#
import unittest


class Solution:
    # @return a tuple, (index1, index2)

    def twoSum(self, num, target):
        """ use extra space """
        dic = {}
        for k, v in enumerate(num):
            if target - v in dic:
                return dic[target - v], k + 1
            dic[v] = k + 1

    # def twoSum(self, num, target):
    #     """
    #     need extra space anyway
    #     and this is n log n because of it's not sorted
    #     """
    #     ivlist = [(v, i + 1) for i, v in enumerate(num)]
    #     ivlist.sort(key=lambda v: v[0])
    #     s, e = 0, len(num) - 1
    #     while s < e:
    #         tmp = ivlist[s][0] + ivlist[e][0]
    #         if tmp == target:
    #             return ivlist[s][1], ivlist[e][1]
    #         elif tmp > target:
    #             e -= 1
    #         elif tmp < target:
    #             s += 1


class Test(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test(self):
        self.assertIsNone(self.s.twoSum([], 9))
        self.assertIsNone(self.s.twoSum([2, 7, 11, 15], 100))
        self.assertEqual(self.s.twoSum([0, 0], 0), (1, 2))
        self.assertEqual(self.s.twoSum([3, 2, 4], 6), (2, 3))
        self.assertEqual(self.s.twoSum([-1, 1], 0), (1, 2))
        self.assertEqual(self.s.twoSum([2, 7, 11, 15], 9), (1, 2))

if __name__ == '__main__':
    unittest.main()
