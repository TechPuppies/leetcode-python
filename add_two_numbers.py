# coding=utf-8
# AC Rate: 23.0%
# SOURCE URL: https://oj.leetcode.com/problems/add-two-numbers/
#
# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain
# a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
import unittest


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode

    def addTwoNumbers(self, l1, l2):
        dummyhead = ListNode(0)
        res, carry = dummyhead, 0
        while l1 and l2:
            c = l1.val + l2.val + carry
            res.next = ListNode(c % 10)
            carry = c / 10
            res, l1, l2 = res.next, l1.next, l2.next
        if l2:
            l1 = l2
        while l1:
            c = l1.val + carry
            res.next = ListNode(c % 10)
            carry = c / 10
            res, l1 = res.next, l1.next
        if carry:
            res.next = ListNode(carry)
        return dummyhead.next


class Test(unittest.TestCase):

    def arrayToList(self, array):
        dummyhead = ListNode(0)
        l1 = dummyhead
        for i in array:
            l1.next = ListNode(i)
            l1 = l1.next
        return dummyhead.next

    def test(self):
        l1 = self.arrayToList([2, 4, 3])
        l2 = self.arrayToList([5, 6, 4])
        s = Solution()
        head = s.addTwoNumbers(l1, l2)
        self.assertEqual(head.val, 7)
        self.assertEqual(head.next.val, 0)
        self.assertEqual(head.next.next.val, 8)


if __name__ == '__main__':
    unittest.main()
