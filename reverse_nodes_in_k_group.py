# coding=utf-8
# AC Rate: 24.8%
# SOURCE URL: https://oj.leetcode.com/problems/reverse-nodes-in-k-group/
#
#
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
#
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# You may not alter the values in the nodes, only nodes itself may be changed.
# Only constant memory is allowed.
#
# For example,
# Given this linked list: 1->2->3->4->5
#
#
# For k = 2, you should return: 2->1->4->3->5
#
#
# For k = 3, you should return: 3->2->1->4->5
#
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        dummy_head = ListNode(0)
        dummy_head.next = head
        start = dummy_head
        while True:
            end = start
            counter = 0 # k = 2
            while end and end.next and counter < k:
                end = end.next
                counter += 1
            if counter == k:
                r = self.reverse(start.next , end)
                start.next = r[0]
                start = r[1]
            else:
                break
        return dummy_head.next

    def reverse(self, start, end):
        tmp = start.next
        if not start.next or start == end:
            return start, start
        start.next = end.next
        s, e = self.reverse(tmp, end)
        e.next = start
        return s, start

if __name__ == '__main__':
    s = Solution()
    head = None
    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    head = s.reverseKGroup(head, 1)
    while head:
        print head.val,
        head = head.next
