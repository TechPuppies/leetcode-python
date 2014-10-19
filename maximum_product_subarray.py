import unittest


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if not A:
            raise ValueError
        if len(A) == 1:
            return A[0]

        m, n, best = 0, 0, float('-inf')
        for i in A:
            if i >= 0:
                m, n = max(m * i, i), n * i
            else:
                m, n = n * i, min(m * i, i)
            best = max(m, best)
        return best



class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.maxProduct([2,3,-2,4]), 6)
        self.assertEqual(s.maxProduct([0.1, 0.1, 2]), 2)
        self.assertEqual(s.maxProduct([-2, 2, -2]), 8)
        self.assertEqual(s.maxProduct([0, -2, 4]), 4)
        self.assertEqual(s.maxProduct([0, -2, -2, 4]), 16)
        self.assertEqual(s.maxProduct([1, -2, 2, 2, 4]), 16)


if __name__ == '__main__':
    unittest.main()
