# coding=utf-8
# AC Rate: 22.1%
# SOURCE URL: https://oj.leetcode.com/problems/permutation-sequence/
#
# The set [1,2,3,…,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"

#
#
# Given n and k, return the kth permutation sequence.
# Note: Given n will be between 1 and 9 inclusive.
#
import math

class Solution:
    # @return a string
    def helper(self, nlist, k, res):
        # print nlist, k, res
        length = len(nlist)
        if length == 0 or k > math.factorial(length):
            return
        elif k > math.factorial(length-1):
            index = (k - 1) / math.factorial(length-1)
            res.append(nlist[index])
            nlist = nlist[:index] + nlist[index+1:]
            k -= index * math.factorial(length-1)
        else:
            res.append(nlist[0])
            nlist = nlist[1:]
        self.helper(nlist, k, res)


    def getPermutation(self, n, k):
        nlist = range(1, n+1)
        res = []
        self.helper(nlist, k, res)
        return ''.join([str(i) for i in res])

if __name__ == '__main__':
    s = Solution()
    print s.getPermutation(4, 3)

