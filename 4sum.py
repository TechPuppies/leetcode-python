# coding=utf-8
# AC Rate: 21.6%
# https://oj.leetcode.com/problems/4sum/

# Given an array S of n integers, are there elements a, b, c, and d in S such
# that a + b + c + d = target? Find all unique quadruplets in the array which
# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤
# The solution set must not contain duplicate quadruplets.
#     For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
#     A solution set is:
#     (-1,  0, 0, 1)
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)
# 
import unittest


class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]

    def pairs(self, num, target):
        res = set()
        pairs = {}
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                s = num[i] + num[j]
                if target - s in pairs:
                    for k in pairs[target - s]:
                        if i > k[1]:
                            res.add((num[k[0]], num[k[1]], num[i], num[j]))
                if s not in pairs:
                    pairs[s] = set()
                pairs[s].add((i, j))
        return [list(i) for i in res]

    def fourSum(self, num, target):
        num.sort()
        return self.pairs(num, target)
        # first thought is dfs with 4 n ** 4 which is stupid


class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.fourSum([0, 0, 0 ,0], 0), [[0, 0, 0, 0]])
        self.assertEqual(s.fourSum([-1, 0, 1], 0), [])
        self.assertEqual(s.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0),
            [[-2, -1, 0, 3], [-3, 0, 1, 2], [-2, -1, 1, 2], [-3, 0, 0, 3],
             [-3, -1, 1, 3], [-2, 0, 0, 2], [-3, -2, 2, 3], [-1, 0, 0, 1]])
        self.assertEqual(s.fourSum([1, 0, -1, 0, -2, 2], 0),
            [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]])
        self.assertEqual(
            s.fourSum([-500,-481,-480,-469,-437,-423,-408,-403,-397,
                       -381,-379,-377,-353,-347,-337,-327,-313,-307,
                       -299,-278,-265,-258,-235,-227,-225,-193,-192,
                       -177,-176,-173,-170,-164,-162,-157,-147,-118,
                       -115,-83,-64,-46,-36,-35,-11,0,0,33,40,51,54,
                       74,93,101,104,105,112,112,116,129,133,146,152,
                       157,158,166,177,183,186,220,263,273,320,328,
                       332,356,357,363,372,397,399,420,422,429,433,
                       451,464,484,485,498,499], 2139), [])


if __name__ == '__main__':
    unittest.main()
