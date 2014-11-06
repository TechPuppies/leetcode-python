# coding=utf-8
# AC Rate: 31.0%
# SOURCE URL: https://oj.leetcode.com/problems/binary-tree-postorder-traversal/
#
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# return [3,2,1].
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
    def postorderTraversal(self, root):
        '''Recursive solution is trivial, could you do it iteratively?'''
        if not root:
            return []
        stack1, res = [root], []
        while stack1:
            node = stack1.pop()
            res.append(node.val)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        return res[::-1]


class Test(unittest.TestCase):

    def setUp(self):
        from helper.tree import Tree
        self.t = Tree()
        self.s = Solution()

    def test(self):
        self.t.load_leetcode_string('{1,#,2,3}')
        self.assertEqual(self.s.postorderTraversal(self.t.head), [3, 2, 1])


if __name__ == '__main__':
    unittest.main()
