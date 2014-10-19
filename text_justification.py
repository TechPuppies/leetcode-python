# coding=utf-8
# AC Rate: 14.0%
# SOURCE URL: https://oj.leetcode.com/problems/text-justification/
#
#
# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
#
#
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
#
#
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
#
#
# For the last line of text, it should be left justified and no extra space is inserted between words.
#
#
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
#
#
# Return the formatted lines as:
#
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#
#
#
# Note: Each word is guaranteed not to exceed L in length.
#
# click to show corner cases.
# Corner Cases:
#
#
# A line other than the last line might contain only one word. What should you do in this case?
# In this case, that line should be left-justified.
#
#
#


class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def genStr(self, A, L):
        space_count = len(A) - 1
        if not space_count:
            return A[0] + ' ' * (L - len(A[0]))
        actual_space_count = L - sum([len(i) for i in A])
        spaces = [' ' * (actual_space_count/space_count)] * space_count
        for i in range(actual_space_count % space_count):
            spaces[i] += ' '
        for k, i in enumerate(spaces):
            A.insert(2 * k + 1, i)
        return ''.join(A)

    def fullJustify(self, words, L):
        res = []
        k, last = 0, 0
        current = 0
        while k < len(words):
            if current + len(words[k]) > L:
                res.append(self.genStr(words[last:k], L))
                last = k
                current = len(words[k]) + 1
            else:
                current += (len(words[k]) + 1)
            k += 1
        l = ' '.join(words[last:])
        l + ' ' * (L - len(l))
        res.append(l + ' ' * (L - len(l)))
        return res

s = Solution()
for i in s.fullJustify(["a","b","c","d","e"], 3):
    print i

for i in s.fullJustify(["This", "is", "an", "justification", "example", "of", "text", "justification."], 16):
    print i

for i in s.fullJustify(["What","must","be","shall","be."], 12):
    print i

for i in s.fullJustify(["Here","is","an","example","of","text","justification."], 14):
    print i
