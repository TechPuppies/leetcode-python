# coding=utf-8
# AC Rate: 23.5%
# SOURCE URL: https://oj.leetcode.com/problems/recover-binary-search-tree/
#
#
# Two elements of a binary search tree (BST) are swapped by mistake.
# Recover the tree without changing its structure.
#
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
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


# Definition for a  binary tree node
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a tree node
    strange = (None, None)

    def find_strange(self, s1, s2):
        if s1.val > s2.val:
            if self.strange[0]:
                self.strange = (self.strange[0], s2)
            else:
                self.strange = (s1, s2)

    def in_order(self, root):
        if not root:
            return []
        res = []
        if root.left:
            res.extend(self.in_order(root.left))
        res.append(root)
        if root.right:
            res.extend(self.in_order(root.right))
        return res

    def recoverTree(self, root):
        if root:
            self.strange = (None, None)
            in_order = self.in_order(root)

            for k in range(1, len(in_order)):
                self.find_strange(in_order[k - 1], in_order[k])

            if None in self.strange:
                return root
            # swap
            s0, s1 = self.strange
            s0.val, s1.val = s1.val, s0.val
        return root


if __name__ == '__main__':
    s = Solution()
    head = TreeNode(2)
    head.left = TreeNode(3)
    head.right = TreeNode(1)
    s.recoverTree(head)
    print(head.val, head.left.val, head.right.val) == (2, 1, 3)

    head = TreeNode(3)
    head.right = TreeNode(2)
    head.right.right = TreeNode(1)
    s.recoverTree(head)
    print(head.val, head.right.val, head.right.right.val) == (1, 2, 3)
