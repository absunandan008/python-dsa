'''
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

'''

class Solution:
    def calculate(self, s: str) -> int:
        #so basically we have 2 variable. One curren and one previous.
        #whenever we see a digit, we save it to result with sign if its addition or substration
        #assign that number to prev and move of
        #if its multiplication or division
        ##first substraction the previous from result because we do not want that
        ##then do prev*curr or prev/curr
        ##then assign prev = curr * prev or prev/curr
        ##set cur to zero after each iteration
        ##return result
        i = 0
        cur = prev = 0
        cur_sign = "+"
        result = 0
        while i < len(s):
            cur_char = s[i]

            if cur_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -= 1
                if cur_sign == "+":
                    result += cur
                    prev = cur
                elif cur_sign == "-":
                    result -= cur
                    prev = -int(cur)
                elif cur_sign == "*":
                    result -= prev
                    result += int(prev * cur)
                    prev = int(prev * cur)
                elif cur_sign == "/":
                    result -= prev
                    result += int(prev / cur)
                    prev = int(prev / cur)
                cur = 0
            else:
                if cur_char != " ":
                    cur_sign = cur_char
            i += 1

        return result

