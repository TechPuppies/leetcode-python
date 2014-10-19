0# coding=utf-8
# AC Rate: 20.8%
# SOURCE URL: https://oj.leetcode.com/problems/merge-intervals/
#
# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
#
#


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '%s %s' % (self.start, self.end)

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals = self.sort_intervals(intervals)
        res = []
        i, j = 0, 1
        while i < len(intervals) and j < len(intervals):
            if intervals[i].end >= intervals[j].start:
                intervals[i].end = max(intervals[i].end, intervals[j].end)
                j += 1
            else:
                res.append(intervals[i])
                i = j
                j += 1
        res.append(intervals[i])
        return res

    def sort_intervals(self, intervals):
        dic = {}
        for i in intervals:
            if i.start not in dic:
                dic[i.start] = i
            else:
                dic[i.start].end = max(dic[i.start].end, i.end)

        print
        return [dic[i] for i in sorted(dic.keys())]


s = Solution()
i1, i2, i3, i4 = Interval(1,4), Interval(0,4), Interval(8,10), Interval(15,18)
for i in s.merge([i1, i2, i3, i4]): print i
