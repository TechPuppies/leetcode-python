# coding=utf-8
# AC Rate: 31.4%
# SOURCE URL: https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/
#
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
#
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
# OJ's Binary Tree Serialization:
#
# The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.
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

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if not root:
            return []
        res, current, queue = [], [], [root]
        next_count, current_count = 0, 1
        while queue:
            node = queue.pop()
            if node.left:
                next_count += 1
                queue.insert(0, node.left)
            if node.right:
                next_count += 1
                queue.insert(0, node.right)
            current.append(node.val)
            current_level -= 1
            if current_count == 0:
                res.insert(0, current)
                current_count = next_count
                next_count = 0
        return res
