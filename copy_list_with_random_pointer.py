# coding=utf-8
# AC Rate: 23.2%
# SOURCE URL: https://oj.leetcode.com/problems/copy-list-with-random-pointer/
#
#
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
#
# Return a deep copy of the list.
#
#


# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            # empty case
            return head

        node = head
        while node:
            # create a copy insert between origin link list nodes
            # 1->2->3 ====> 1->copied(1)->2->copied(2)->3->copied(3)
            tmp = node.next
            node.next = RandomListNode(node.label)
            node.next.next = tmp
            node = tmp

        node = head
        while node:
            # so then original_node.next.random -> original_node.random.next
            if node.random:
                node.next.random = node.random.next
            node = node.next.next


        node = head
        copy_head = head.next
        while node and node.next:
            # detach two list, link copies together
            temp = node.next
            node.next = node.next.next # detach
            if node.next:
                temp.next = node.next.next # re-link copies
            node = node.next

        return copy_head
