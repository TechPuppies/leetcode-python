# coding=utf-8
# AC Rate: 22.0%
# SOURCE URL: https://oj.leetcode.com/problems/rotate-list/
#
# Given a list, rotate the list to the right by k places, where k is non-negative.
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
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
    def rotateRight(self, head, k):
        if not head:
            return head
        node = head
        counter = 1
        while node.next:
            node = node.next
            counter += 1
        # node is the last one now
        node.next = head
        # print node.val
        # cycle

        runner1 = head
        runner2 = head
        for i in range(k):
            runner1 = runner1.next

        while runner1 != head:
            runner1 = runner1.next
            runner2 = runner2.next

        # now runner2 is the last kth
        # todo put them togher
        node = runner2
        counter -= 1
        while counter:
            counter -= 1
            node = node.next
        node.next = None
        return runner2



if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    head = s.rotateRight(head, 1)
    while head:
        print head.val,
        head = head.next

