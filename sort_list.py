# coding=utf-8
# AC Rate: 20.4%
# SOURCE URL: https://oj.leetcode.com/problems/sort-list/
#
# Sort a linked list in O(n log n) time using constant space complexity.
#


import unittest


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        res, node = [], self
        while node:
            res.append(node.val)
            node = node.next
        return res

    @classmethod
    def gen(cls, A):
        dummyhead = cls(None)
        node = dummyhead
        for i in A:
            node.next = cls(i)
            node = node.next
        return dummyhead.next


class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def sortList(self, head):
        return self.merge_sort(head, self.get_length(head))

    def merge_sort(self, head, length):
        if not head or length <= 1:
            return head
        right_head = self.get_right_head(head, length)
        left = self.merge_sort(head, length / 2)
        right = self.merge_sort(right_head, length - length / 2)
        head = self.merge(left, right)
        return head

    def merge(self, h1, h2):
        if not h1 or not h2:
            return h1 or h2
        if h1.val > h2.val:
            h1, h2 = h2, h1
        head, node = h1, h1
        h1 = h1.next
        while h1 and h2:
            if h1.val < h2.val:
                node.next = h1
                h1 = h1.next
            else:
                node.next = h2
                h2 = h2.next
            node = node.next
            node.next = None
        if h2:
            h1 = h2
        if h1:
            node.next = h1
        return head

    def get_right_head(self, head, length):
        if length < 2 or not head:
            return None
        length = (length) / 2
        tmp, node = None, head
        while length:
            tmp = node
            node = node.next
            length -= 1
        if tmp:
            tmp.next = None
        return node

    def get_length(self, head):
        tmp, c = head, 0
        while tmp:
            tmp = tmp.next
            c += 1
        return c


class Test(unittest.TestCase):

    def unit(self, A):
        head = ListNode.gen(A)
        head = self.s.sortList(head)
        self.assertEqual(self.s.get_length(head), len(A))
        if head:
            self.assertEqual(head.to_list(), sorted(A))

    def test(self):
        self.s = Solution()
        self.unit([5, 6, 7, 1, 2, 3, 0])
        self.unit([])
        self.unit([1, 1, 1, 1])
        self.unit([0, 1, 1, 0])


if __name__ == '__main__':
    unittest.main()
