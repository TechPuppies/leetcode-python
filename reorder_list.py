# coding=utf-8
# AC Rate: 20.3%
# SOURCE URL: https://oj.leetcode.com/problems/reorder-list/
#
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
#
#


# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return nothing

    def reorderList(self, head):
        if not head:
            return head
        walker = head
        runner = head
        while walker.next and runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next

        end = runner.next if runner.next else runner

        mid = walker
        mid.next = self.reverse(mid.next)
        walker = mid.next
        # reverse mid.next to end
        node = head
        while node and walker:
            temp_walker = walker.next
            walker.next = node.next
            node.next = walker
            node = walker.next
            if node == end:
                walker.next = None
            if node and node.next == end:
                node.next = None
            walker = temp_walker


    def reverse(self, start):
        # reverse start + 1 to end
        if not start:
            return
        p1 = start
        p2 = start.next
        while p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        start.next = p2
        return p1

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
s.reorderList(head)
while head:
    print head.val,
    head = head.next
