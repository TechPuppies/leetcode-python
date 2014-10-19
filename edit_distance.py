# coding=utf-8
# AC Rate: 25.2%
# SOURCE URL: https://oj.leetcode.com/problems/edit-distance/
#
#
# Given two words word1 and word2, find the minimum number of
# steps required to convert word1 to word2.
# (each operation is counted as 1 step.)
#
#
# You have the following 3 operations permitted on a word:
#
#
# a) Insert a character
# b) Delete a character
# c) Replace a character
#
#
import unittest


class Solution:
    # @return an integer

    def minDistance(self, w1, w2):
        lenw1, lenw2 = len(w1) + 1, len(w2) + 1
        d = [[-1] * (lenw1) for i in range(lenw2)]
        for i in range(lenw1):
            d[0][i] = i
        for i in range(lenw2):
            d[i][0] = i
        for i in range(1, lenw2):
            for j in range(1, lenw1):
                if w1[j-1] == w2[i-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = min(d[i][j-1], d[i-1][j], d[i-1][j-1]) + 1
        return d[-1][-1]

    def minChanges(self, w1, w2):
        # status < left, ^ top, \ lefttop

        lenw1, lenw2 = len(w1) + 1, len(w2) + 1
        d = [[-1] * (lenw1) for i in range(lenw2)]
        for i in range(lenw1):
            d[0][i] = (i, '<')
        for i in range(lenw2):
            d[i][0] = (i, '^')
        for i in range(1, lenw2):
            for j in range(1, lenw1):
                if w1[j-1] == w2[i-1]:
                    d[i][j] = (d[i-1][j-1][0], '\\')
                else:
                    minimum, direction = d[i-1][j-1][0], '\\'
                    if d[i][j-1][0] < minimum:
                        minimum, direction = d[i][j-1][0], '<'
                    if d[i-1][j][0] < minimum:
                        minimum, direction = d[i-1][j][0], '^'
                    d[i][j] = (minimum + 1, direction)

        i, j = lenw2 - 1, lenw1 - 1
        res = [w1]
        while i or j:
            if d[i][j][1] == '\\':
                i -= 1
                j -= 1
                if not w1[j] == w2[i]:
                    w1 =  w1[:j] + w2[i] + w1[j+1:]
                    res.append(w1)
            elif d[i][j][1] == '<':
                j -= 1
                w1 = w1[:j] + w1[j+1:]
                res.append(w1)
            else:
                i -= 1
                w1 = w1 + w2[i]
                res.append(w1)
        for i in res:
            print i

    def allMinChanges(self, w1, w2):

        lenw1, lenw2 = len(w1) + 1, len(w2) + 1
        d = [[-1] * (lenw1) for i in range(lenw2)]
        for i in range(lenw1):
            d[0][i] = i
        for i in range(lenw2):
            d[i][0] = i
        for i in range(1, lenw2):
            for j in range(1, lenw1):
                if w1[j-1] == w2[i-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = min(d[i][j-1], d[i-1][j], d[i-1][j-1]) + 1

        for i in d:
            print i

        stack = [(0, 0, [w1])]
        while stack:
            i, j, path = stack.pop()
            print i, j
            if path[-1] == w2:
                print path
                continue
            # if d[i+1][j] == d[i][j] or d[i][j+1] == d[i][j] or (d[i+1][j+1] == d[i][j] and w1[j] != w2[i]):
            #     continue
            if i + 1 < lenw2 and d[i+1][j] == d[i][j] + 1 :#and d[i][j] < d[-1][-1]:
                current = path[-1][:j] + w2[i] + path[-1][j:]
                stack.append((i+1, j, path + [current]))
            if j + 1 < lenw1 and d[i][j+1] == d[i][j] + 1:# and d[i][j] < d[-1][-1]:
                current = path[-1][:j] + path[-1][j+1:]
                stack.append((i, j+1, path + [current]))
            if i + 1 < lenw2 and j + 1 < lenw1 and d[i+1][j+1] == d[i][j] + 1:# and d[i][j] < d[-1][-1]:
                current = path[-1][:j] + w2[i] + path[-1][j+1:]
                stack.append((i+1, j+1, path + [current]))
            if i + 1 < lenw2 and j + 1 < lenw1 and d[i+1][j+1] == d[i][j] and w1[j] == w2[i]:# and d[i][j] <= d[-1][-1]:
                stack.append((i+1, j+1, path))

class Test(unittest.TestCase):

    def test(self):
        w1 = 'dinitrophenylhydrazine'
        w2 = 'acetylphenylhydrazine'
        s = Solution()
        s.allMinChanges('dinitrop', 'acetylp')
        self.assertEqual(s.minDistance(w1, w2), 6)
        self.assertEqual(s.minDistance('DOTA', 'THAT'), 4)


if __name__ == '__main__':
    unittest.main()
