# coding=utf-8
# AC Rate: 20.5%
# SOURCE URL: https://oj.leetcode.com/problems/insert-interval/
#
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.
#
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
#
#
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
#
#
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
#
#


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '(%d, %d)' % (self.start, self.end)

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def shouldMerge(self, interval, newInterval):
        return (newInterval.start >= interval.start and \
                newInterval.start <= interval.end) or \
            (newInterval.end >= interval.start and \
                newInterval.end <= interval.end) or \
            (newInterval.start <= interval.start and \
                newInterval.end >= interval.end)


    def insert(self, intervals, newInterval):
        merging = Interval(newInterval.start, newInterval.end)
        res = []
        for i in intervals:
            if merging and i.start > merging.end:
                res.append(merging)
                merging = None
            if merging and self.shouldMerge(i, newInterval):
                merging.start = min(merging.start, i.start)
                merging.end = max(merging.end, i.end)
            else:
                res.append(i)
        if merging:
            res.append(merging)
        return res

s = Solution()
for i in s.insert([Interval(2, 5),Interval(6, 7),Interval(8, 9),], Interval(0, 1)):
    print i,
print
for i in s.insert([Interval(1, 5),], Interval(6, 9)):
    print i,
print
for i in s.insert([Interval(1, 5),], Interval(0, 0)):
    print i,
print
for i in s.insert([Interval(1, 2),Interval(3, 5),Interval(6, 7),Interval(8, 10),Interval(12, 16)], Interval(4, 9)):
    print i,
print
