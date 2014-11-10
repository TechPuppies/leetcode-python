# coding=utf-8
# AC Rate: 26.4%
# SOURCE URL: https://oj.leetcode.com/problems/construct-binary-tree-from-
# preorder-and-inorder-traversal/
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# Note:
# You may assume that duplicates do not exist in the tree.
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
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node

    def buildTree(self, preorder, inorder):
        if not preorder and not inorder:
            return None
        root, lefts = TreeNode(preorder[0]), inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:lefts + 1], inorder[:lefts])
        root.right = self.buildTree(preorder[lefts+1:], inorder[lefts+1:])
        return root


class Test(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test(self):
        root = self.s.buildTree([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.left.left.val, 4)
        self.assertEqual(root.left.right.val, 5)
        self.assertEqual(root.right.left.val, 6)
        self.assertEqual(root.right.right.val, 7)


if __name__ == '__main__':
    unittest.main()
