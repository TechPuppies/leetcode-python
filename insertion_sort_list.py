# coding=utf-8
# AC Rate: 25.3%
# SOURCE URL: https://oj.leetcode.com/problems/insertion-sort-list/
#
# Sort a linked list using insertion sort.
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        p1_prev = head
        p1 = head.next
        while p1:
            tmp = p1.next
            if p1_prev.val > p1.val:
                p2_prev = None
                p2 = head
                while p1.val > p2.val:
                    p2_prev = p2
                    p2 = p2.next

                if not p2_prev:
                    # head
                    head = p1
                else:
                    # p2.next = p1.next  this is wrong
                    p2_prev.next = p1
                p1_prev.next = p1.next
                p1.next = p2
            else:
                p1_prev = p1_prev.next
            p1 = tmp
        return head
