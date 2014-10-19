# coding=utf-8
# AC Rate: 19.8%
# SOURCE URL: https://oj.leetcode.com/problems/simplify-path/
#
# Given an absolute path for a file (Unix-style), simplify it.
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
#
# click to show corner cases.
# Corner Cases:
#
#
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
#
#
#


class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        current = []
        simplifiedPath = []
        for i in path + '/':
            if i == '/':
                c = ''.join(current)
                if c and c != '.':
                    if c == '..':
                        if simplifiedPath:
                            simplifiedPath.pop()
                    else:
                        simplifiedPath.append(c)
                current = []
            else:
                current.append(i)
        return '/' + '/'.join(simplifiedPath)

s = Solution()
print s.simplifyPath('/...')
print s.simplifyPath('/home//foo/')
print s.simplifyPath('/home/')
print s.simplifyPath('/a/./b/../../c/')
