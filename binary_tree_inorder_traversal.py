# coding=utf-8
# AC Rate: 35.6%
# SOURCE URL: https://oj.leetcode.com/problems/binary-tree-inorder-traversal/
#
# Given a binary tree, return the inorder traversal of its nodes' values.
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
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized
# on OJ.
# OJ's Binary Tree Serialization:
#
# The serialization of a binary tree follows a level order traversal, where '#'
# signifies a path terminator where no node exists below.
#
#
# Here's an example:
#
#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
#
# The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
#
#
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

    def inorderTraversal(self, root):
        return self.inorderTraversalHelper(root)

    def inorderTraversalHelper(self, root):
        res = []
        if not root:
            return res
        res += self.inorderTraversalHelper(root.left)
        res += [root.val]
        res += self.inorderTraversalHelper(root.right)
        return res

    def inorderTraversalWithoutRecursion(self, root):
        res, stack, current = [], [], root
        while True:
            while current:
                stack.append(current)
                current = current.left
            if stack:
                node = stack.pop()
                res.append(node.val)
                current = node.right
            else:
                break
        return res


class Test(unittest.TestCase):

    def test(self):
        from helper.tree import Tree
        t = Tree()
        t.load_leetcode_string('{1,2,3,#,#,4,#,#,5}')
        s = Solution()
        self.assertEqual(s.inorderTraversal(t.head),
                         [2, 1, 4, 5, 3])
        self.assertEqual(s.inorderTraversalWithoutRecursion(t.head),
                         [2, 1, 4, 5, 3])

if __name__ == '__main__':
    unittest.main()
