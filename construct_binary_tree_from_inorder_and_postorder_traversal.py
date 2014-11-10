# coding=utf-8
# AC Rate: 26.4%
# SOURCE URL: https://oj.leetcode.com/problems/construct-binary-tree-from-inorde
# r-and-postorder-traversal/
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
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
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node

    def buildTree(self, inorder, postorder):
        if not postorder and not inorder:
            return None
        root, lefts = TreeNode(postorder[-1]), inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:lefts], postorder[:lefts])
        root.right = self.buildTree(inorder[lefts + 1:], postorder[lefts:-1])
        return root


class Test(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test(self):
        root = self.s.buildTree([4, 2, 5, 1, 6, 3, 7], [4, 5, 2, 6, 7, 3, 1])
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.left.left.val, 4)
        self.assertEqual(root.left.right.val, 5)
        self.assertEqual(root.right.left.val, 6)
        self.assertEqual(root.right.right.val, 7)

    def test2(self):
        root = self.s.buildTree([1], [1])
        self.assertEqual(root.val, 1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test3(self):
        root = self.s.buildTree([], [])
        self.assertIsNone(root)

    def test4(self):
        root = self.s.buildTree([1, 3, 2], [3, 2, 1])
        self.assertEqual(root.val, 1)
        self.assertEqual(root.right.val, 2)
        self.assertEqual(root.right.left.val, 3)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right.right)

if __name__ == '__main__':
    unittest.main()
