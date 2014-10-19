# coding=utf-8
# AC Rate: 24.9%
# SOURCE URL: https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
#
#
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
#
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        dummy_head = ListNode(None)
        dummy_head.next = head
        p1 = dummy_head
        while p1:
            if (p1.next) and (p1.next.next) and p1.next.next.val == p1.next.val:
                worker = p1.next.next
                while worker.next and worker.next.val == worker.val:
                    worker = worker.next
                p1.next = worker.next
            else:
                p1 = p1.next
        return dummy_head.next

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(2)
    # head.next.next.next.next.next = ListNode(4)
    # head.next.next.next.next.next.next = ListNode(4)

    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(3)
    # head.next.next.next.next = ListNode(4)
    # head.next.next.next.next.next = ListNode(4)
    # head.next.next.next.next.next.next = ListNode(5)
    head = s.deleteDuplicates(head)
    while head:
        print head.val
        head = head.next
