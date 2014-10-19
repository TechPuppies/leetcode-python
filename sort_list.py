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
        return self.sortHelper(head, self.get_length(head))[0]

    def sortHelper(self, head, length):
        h, _ = self.sortHelper(head, length/2)
        _, t = self.sortHelper(_.next, length/2)
        self.merge()
        return h, t

    def get_length(self, head):
        c = 0
        while head:
            head = head.next
            c += 1
        return c


class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        A = [5,6]#,7,1,2,3,0]
        head = ListNode.gen(A)
        res = []
        head = s.sortList(head)
        # while head:
        #     res.append(head.val)
        #     head = head.next
        self.assertEqual(res, [0,1,2,3,5,6,7])

if __name__ == '__main__':
    unittest.main()
    # pass
