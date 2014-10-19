# coding=utf-8
# AC Rate: 20.0%
# SOURCE URL: https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/
#
#
# Given a binary tree, find the maximum path sum.
#
#
# The path may start and end at any node in the tree.
#
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
#
#
#
# Return 6.
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
    # @return an integer
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        return self.helper(root)[1]

    def helper(self, root):
        if not root:
            return 0, float('-inf')

        leftRoad, leftPath = self.helper(root.left)
        rightRoad, rightPath = self.helper(root.right)

        return (max([0, root.val, root.val + leftRoad, root.val + rightRoad]),
            max([leftPath, rightPath, leftRoad + root.val + rightRoad]))
            
# THIS IS THE JAVA CODE AC
# CANNTO GET MY PYTHON CODE AC
# ANYONE HAVE IDEA?
# /**
#  * Definition for binary tree
#  * public class TreeNode {
#  *     int val;
#  *     TreeNode left;
#  *     TreeNode right;
#  *     TreeNode(int x) { val = x; }
#  * }
#  */
# public class Solution {
#     Map<TreeNode, Integer> roadDP = new HashMap<TreeNode, Integer>();
#     Map<TreeNode, Integer> pathDP = new HashMap<TreeNode, Integer>();
#
#     public int maxPathSum(TreeNode root) {
#         return helper(root);
#     }
#     public int maxRoad(TreeNode root){
#         if(root == null){
#             return 0;
#         }
#         if(!this.roadDP.containsKey(root)){
#             int best =  Math.max(0, root.val);
#             best = Math.max(best, root.val + maxRoad(root.left));
#             best = Math.max(best, root.val + maxRoad(root.right));
#             this.roadDP.put(root, best);
#         }
#         return this.roadDP.get(root);
#     }
#     public int helper(TreeNode root){
#         if(root == null) return Integer.MIN_VALUE;
#         if(!this.pathDP.containsKey(root)){
#             int best = Math.max(helper(root.left), helper(root.right));
#             best = Math.max(best, maxRoad(root.left)+root.val+maxRoad(root.right));
#             this.pathDP.put(root, best);
#         }
#         return this.pathDP.get(root);
#     }
# }
