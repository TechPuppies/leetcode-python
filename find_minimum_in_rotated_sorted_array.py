# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
import unittest


class Solution:
    # @param num, a list of integer
    # @return an integer

    def findMin(self, num):
        # find mid
        if not num:
            return None

        def helper(num, start, end):
            # Base case
            if num[start] <= num[end]:
                return num[start]
            mid = start + (end - start) / 2
            if num[mid] >= num[start]:
                return helper(num, mid + 1, end)
            if num[mid] <= num[end]:
                return helper(num, start, mid)
        return helper(num, 0, len(num) - 1)


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.findMin([1, 2, 3, 4, 5]), 1)
        self.assertEqual(s.findMin([5, 1, 2, 3, 4]), 1)
        self.assertEqual(s.findMin([2, 2, 2, 1, 1]), 1)
        self.assertEqual(s.findMin([1, 1, 1, 1, 1]), 1)
        self.assertEqual(s.findMin([1, 2, 3, 1, 1]), 1)
        self.assertEqual(s.findMin([2, 3, 1, 1, 1]), 1)


if __name__ == '__main__':
    unittest.main()
