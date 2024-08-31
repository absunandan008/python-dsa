"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""

class Solution:
    def calculate(self, s: str) -> int:
        def helper(s, index):
            stack = []
            prev_sign = "+"
            num = 0

            while index < len(s):
                cur_char = s[index]

                if cur_char.isdigit():
                    num = num * 10 + int(cur_char)

                if cur_char == "(":
                    num, index = helper(s, index + 1)

                if cur_char in "+-" or cur_char == ")" or index == len(s) - 1:
                    if prev_sign == "+":
                        stack.append(num)
                    elif prev_sign == "-":
                        stack.append(-num)
                    num = 0
                    prev_sign = cur_char

                if cur_char == ")":
                    break

                index += 1

            return sum(stack), index

        return helper(s, 0)[0]

    def calculate_not_good(self, s: str) -> int:
        stack = []
        num = 0
        sign  = "+"
        i = 0
        while i < len(s):
            cur_char = s[i]

            if cur_char.isdigit():
                num = num * 10 + int(cur_char)

            if cur_char == "(":
                #save state in a variable
                j = i
                balance = 0
                # find the corresponding ')'
                while i < len(s):
                    #this is same ( where we entered the loop when it encounters first time
                    if s[i] == "(":
                        balance += 1
                    if s[i] == ")":
                        balance -= 1
                    if balance == 0:
                        break
                    i += 1
                #recursive call and get then sum inside
                num = self.calculate(s[j+1:i])

            if cur_char in "+-" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                if sign == "-":
                    stack.append(-num)
                num = 0
                sign = cur_char
            i += 1
        return sum(stack)
