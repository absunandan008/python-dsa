"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.


Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_digit = []
        for token in tokens:
            if token in "+-/*":
                number_1 = stack_digit.pop()
                number_2 = stack_digit.pop()
                if token == "+":
                    stack_digit.append(number_1 + number_2)
                elif token == "-":
                    stack_digit.append(number_1 - number_2)
                elif token == "*":
                    stack_digit.append(number_1 * number_2)
                elif token == "/":
                    stack_digit.append(int(number_1 / number_2))
            else:
                stack_digit.append(int(token))

        return stack_digit.pop()