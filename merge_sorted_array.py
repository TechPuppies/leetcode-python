# coding=utf-8
# AC Rate: 32.1%
# SOURCE URL: https://oj.leetcode.com/problems/merge-sorted-array/
# 
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
# 
# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
# 


class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        