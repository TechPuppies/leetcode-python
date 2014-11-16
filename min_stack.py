# coding=utf-8
# Add Date: 2014-11-09
# Acceptance: 15.5%
# Difficulty: Easy
# SourceUrl: https://oj.leetcode.com/problems/min-stack/
# Design a stack that supports push, pop, top, and
# retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
import unittest


class MinStack:
    '''
    This solution got MLE in Leetcode!!!!
    I believe there is one solution use less memory, use two stacks
    But is O(n) space anyway, will code that when I have a chance
    '''
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self._data = []

    def push(self, x):
        if self.getMin():
            self._data.append((x, min(self.getMin(), x)))
        else:
            self._data.append((x, x))

    # @return nothing
    def pop(self):
        tmp = None
        if self._data:
            tmp = self._data.pop()[0]
        return tmp

    # @return an integer
    def top(self):
        if self._data:
            return self._data[-1][0]
        return None

    # @return an integer
    def getMin(self):
        if self._data:
            return self._data[-1][1]
        return None


class Test(unittest.TestCase):

    def setUp(self):
        self.minstack = MinStack()

    def test(self):
        s = self.minstack
        s.push(1)
        self.assertEqual(s.top(), 1)
        self.assertEqual(s.getMin(), 1)
        s.push(0)
        self.assertEqual(s.top(), 0)
        self.assertEqual(s.getMin(), 0)
        self.assertEqual(s.pop(), 0)
        self.assertEqual(s.getMin(), 1)
        self.assertEqual(s.top(), 1)


if __name__ == '__main__':
    unittest.main()
