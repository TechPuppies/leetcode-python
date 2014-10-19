# coding=utf-8
# AC Rate: 22.9%
# SOURCE URL: https://oj.leetcode.com/problems/valid-palindrome/
#
#
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.
#
#


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        # use extra space `tmp`
        tmp = []
        for i in s:
            if (ord(i) >= 65 and ord(i) <= 90) \
                or (ord(i) >= 97 and ord(i)<=122) \
                or (ord(i) >= 48 and ord(i)<=57):
                # get only A-Za-z1-9
                tmp.append(i.lower())

        for i in range(len(tmp)/2):
            # check palindrome
            if tmp[i] != tmp[len(tmp) - 1 - i]:
                return False
        return True


s = Solution()
print s.isPalindrome('`l;`` 1o1 ??;l`')
print s.isPalindrome('race a car')
print s.isPalindrome('A man, a plan, a canal: Panama')
