# coding=utf-8
# AC Rate: 21.8%
# SOURCE URL: https://oj.leetcode.com/problems/merge-k-sorted-lists/
#
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
#


# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param a list of ListNode
    # @return a ListNode

    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        new_lists = []
        for i in range((len(lists) + 1) / 2):
            if i == len(lists) - 1 - i:
                new_lists.append(lists[i])
            else:
                new_lists.append(self.merge2Lists(lists[i],
                                                  lists[len(lists) - 1 - i]))

        return self.mergeKLists(new_lists)

    def merge2Lists(self, list1, list2):
        dummyhead = ListNode(0)
        new = dummyhead
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val < p2.val:
                new.next = p1
                p1 = p1.next
            else:
                new.next = p2
                p2 = p2.next
            new = new.next
        if p1:
            new.next = p1
        if p2:
            new.next = p2
        return dummyhead.next


s = Solution()
lists = [ListNode(i) for i in range(100)]
head = s.mergeKLists(lists)
while head:
    print head.val,
    head = head.next
