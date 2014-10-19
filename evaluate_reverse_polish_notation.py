# coding=utf-8
# AC Rate: 19.9%
# SOURCE URL: https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/
#
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
#
# Some examples:
#
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
#
#
#
import math

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def ezCalc(self, p1, p2, o):
        p1, p2 = int(p1), int(p2)
        # print p1, p2, o
        if o == '+':
            return (p1) + (p2)
        elif o == '-':
            return (p1) - (p2)
        elif o == '*':
            return (p1) * (p2)
        elif o == '/':
            if p1 < 0 and p2 > 0:
                return -(abs((p1))/(p2))
            elif p2 < 0 and p1 > 0:
                return -((p1)/abs((p2)))
            else:
                return (p1) / (p2)
        else:
            raise ValueError

    def evalRPN(self, tokens):

        if len(tokens) == 1:
            return int(tokens[0])

        ops = set(['+', '-', '*', '/'])
        stack = []
        for i in tokens:
            if i in ops:
                # todo stack is empty check
                p2 = stack.pop()
                p1 = stack.pop()
                stack.append(self.ezCalc(p1, p2, i))
            else:
                stack.append(i)
        return stack.pop()

s = Solution()
print s.evalRPN(["18"]) == 18
print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
print s.evalRPN(["2", "1", "+", "3", "*"]) == 9
print s.evalRPN(["4", "13", "5", "/", "+"]) == 6
