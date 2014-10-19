# coding=utf-8
# AC Rate: 29.8%
# SOURCE URL: https://oj.leetcode.com/problems/sum-root-to-leaf-numbers/
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
# For example,
#
#     1
#    / \
#   2   3
#
#
#
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
#
# Return the sum = 12 + 13 = 25.
#
#


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        res = 0
        if not root:
            return res
        stack = [(root, [root.val])]
        while stack:
            node, current = stack.pop()
            if not node.left and not node.right:
                cv = 0
                for i in current:
                    cv = i + cv * 10
                res += cv
            else:
                if node.left:
                    stack.append((node.left, current + [node.left.val]))
                if node.right:
                    stack.append((node.right, current + [node.right.val]))
        return res
