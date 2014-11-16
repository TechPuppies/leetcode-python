# coding=utf-8
# AC Rate: 28.1%
# SOURCE URL:
# https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/
#
#
# Given a binary tree, flatten it to a linked list in-place.
#
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
#
#
#
# The flattened tree should look like:
#
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
#
# click to show hints.
# Hints:
# If you notice carefully in the flattened tree, each node's right child
# points to the next node of a pre-order traversal.
#
#
import unittest


# Definition for a  binary tree node
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # @param root, a tree node
    # @return nothing, do it in place

    def flattenHelper(self, root):
        ''' return the flaten head and tail '''
        if not root:
            return None, None
        left_flatten = self.flattenHelper(root.left)
        right_flatten = self.flattenHelper(root.right)
        root.left, tail = None, root
        if left_flatten[0]:
            tail.right, tail = left_flatten
        if right_flatten[0]:
            tail.right, tail = right_flatten
        return root, tail

    def flatten(self, root):
        ''' use recursion '''
        return self.flattenHelper(root)[0]


class Test(unittest.TestCase):

    def test(self):
        from helper.tree import Tree
        t = Tree()
        t.load_leetcode_string('{1,2,5,3,4,#,6}')
        s = Solution()
        s.flatten(t.head)
        self.assertEqual(t.head.val, 1)
        self.assertEqual(t.head.right.val, 2)
        self.assertEqual(t.head.right.right.val, 3)
        self.assertEqual(t.head.right.right.right.val, 4)

if __name__ == '__main__':
    unittest.main()
