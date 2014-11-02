# coding=utf-8
# AC Rate: 17.3%
# SOURCE URL: https://oj.leetcode.com/problems/median-of-two-sorted-arrays/
#
# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
#
import unittest


class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        # shorter one is A
        n, m = len(A), len(B)
        if n > m:
            return self.findMedianSortedArrays(B, A)

        k = (n + m - 1) / 2

        # binary search
        can = self.binarySearchHelper(A, B, 0, n, k)
        candidates = []
        candidates.append(A[can] if can < n else float('inf'))
        candidates.append(A[can-1] if can > 0 else float('-inf'))
        candidates.append(B[k-can+1] if k-can+1 < m else float('inf'))
        candidates.append(B[k-can] if k-can >= 0 else float('-inf'))
        if (n + m) % 2 == 0:
            return float(max(candidates[1], candidates[3]) \
                + min(candidates[0], candidates[2])) / 2
        else:
            return max(candidates[1], candidates[3])

    def binarySearchHelper(self, A, B, start, end, k):
        if start >= end:
            return start
        mid = start + (end - start) / 2

        if mid < 0 or A[mid] < B[k - mid]:
            return self.binarySearchHelper(A, B, mid + 1, end, k)
        else:
            return self.binarySearchHelper(A, B, start, mid, k)

class Test(unittest.TestCase):

    def test(self):

        s = Solution()
        A = [1, 3, 5, 7, 9]
        B = [2, 4, 6, 8]
        self.assertEqual(s.findMedianSortedArrays(A, B), 5)
        B = [2, 4, 6, 8, 10]
        self.assertEqual(s.findMedianSortedArrays(A, B), 5.5)
        A = [1, 3, 5]
        self.assertEqual(s.findMedianSortedArrays(A, B), 4.5)


if __name__ == '__main__':

    unittest.main()
