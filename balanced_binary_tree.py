# coding=utf-8
# AC Rate: 32.7%
# SOURCE URL: https://oj.leetcode.com/problems/balanced-binary-tree/
#
# Given a binary tree, determine if it is height-balanced.
#
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
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
    # @return a boolean
    def isBalanced(self, root):
        return self.helper(root) >= 0

    def helper(self, root):
        # recursion
        if not root:
            return 0
        bl = self.helper(root.left)
        if bl < 0:
            return -1
        br = self.helper(root.right)
        if br < 0:
            return -1
        if abs(bl - br) > 1:
            return -1
        return max(bl, br) + 1


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertFalse(s.isBalanced(root))
        root.right = TreeNode(4)
        self.assertTrue(s.isBalanced(root))
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(4)
        self.assertTrue(s.isBalanced(root))
        root.left.left = None
        self.assertTrue(s.isBalanced(root))
        root.right.right.left = TreeNode(4)
        self.assertFalse(s.isBalanced(root))


if __name__ == '__main__':
    unittest.main()
