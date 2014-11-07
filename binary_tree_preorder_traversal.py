# coding=utf-8
# AC Rate: 35.6%
# SOURCE URL: https://oj.leetcode.com/problems/binary-tree-preorder-traversal/
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#
#    1
#     \
#      2
#     /
#    3
#
#
#
# return [1,2,3].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import unittest


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if not root:
            return []
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


class Test(unittest.TestCase):

    def setUp(self):
        from helper.tree import Tree
        self.t = Tree()
        self.s = Solution()

    def test(self):
        self.t.load_leetcode_string('{1,2,3,4,5,6,7}')
        self.assertEqual(self.s.preorderTraversal(self.t.head),
                         [1, 2, 4, 5, 3, 6, 7])


if __name__ == '__main__':
    unittest.main()
