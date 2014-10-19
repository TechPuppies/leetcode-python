# coding=utf-8
# AC Rate: 10.9%
# SOURCE URL: https://oj.leetcode.com/problems/max-points-on-a-line/
#
# Given n points on a 2D plane,
# find the maximum number of points that lie on the same straight line.
#
import unittest


class Point:

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    # @param points, a list of Points
    # @return an integer

    def maxPoints(self, points):
        # how to define a line?
        if len(points) <= 2:
            return len(points)
        dic, best = {}, 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                k, c = self.line_key(points[i], points[j])
                if k not in dic:
                    dic[k] = {}
                if c not in dic[k]:
                    dic[k][c] = set()
                dic[k][c].add(i)
                dic[k][c].add(j)
                best = max(len(dic[k][c]), best)
        return best

    def line_key(self, p1, p2):
        if p1.x == p2.x:
            return float('inf'), p1.x
        diffx = float(p1.x - p2.x)
        return float(p1.y - p2.y)/diffx, float(p2.y * p1.x - p1.y * p2.x)/diffx


class Test(unittest.TestCase):

    def test(self):
        points = [
            Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 4), Point(4, 5),
            Point(0, 1), Point(3, 1), Point(7, 2), Point(8, 4), Point(0, 5),
            Point(0, 10), Point(2, 1), Point(4, 6), Point(4, 4), Point(1, 5),
            Point(0, 4), Point(4, 3), Point(2, 2), Point(9, 4), Point(2, 5),
        ]
        s = Solution()
        self.assertEqual(s.line_key(points[0], points[1]), (1, 0))
        print s.maxPoints(points)


if __name__ == '__main__':
    unittest.main()
