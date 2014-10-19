# coding=utf-8
# AC Rate: 21.8%
# SOURCE URL: https://oj.leetcode.com/problems/implement-strstr/
#
#
# Implement strStr().
#
#
# Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
#
#

# Return Value !!!
# Which means instead of returning the index i, we return haystack[i:]

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None

    def strStr(self, haystack, needle):
        m = [[False] * (len(haystack) + 1 - len(needle))
             for i in range(len(needle) + 1)]

        for k in range(len(m[0])):
            m[0][k] = True

        for i in range(1, len(needle) + 1):
            for j in range(0, len(haystack) + 1 - len(needle)):
                if not m[i -1][j]:
                    m[i][j] = False
                else:
                    m[i][j] = (haystack[i + j - 1] == needle[i - 1])

        try:
            return  haystack[m[-1].index(True):]
        except ValueError:
            return None

s = Solution()
# print s.strStr('', '') == ''
print s.strStr('a', 'a') == 'a'
# print s.strStr(''.join(['a'] * 1000000) + 'b', 'ab') == 'ab'
# print s.strStr('abcdefg', 'cd') == "cdefg"
# print s.strStr('aaaabbbababb', 'baa') == None
# print s.strStr('heror', 'herehero') == None
# print s.strStr('herehero', 'heror') == None
