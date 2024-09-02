"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros
until a non-digit character is encountered or the end of the string is reached.
If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231,
and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

"""
from unicodedata import digit


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        sign_found = False
        result = 0
        index = 0
        n = len(s)

        INT_MAX = pow(2,31) - 1
        INT_MIN = -pow(2, 31)

        while index < n and s[index] == " ":
            index += 1

        if index < n and s[index] == "+":
            sign = 1
            index += 1
            sign_found = True

        if index < n and s[index] == "-" and not sign_found:
            sign = -1
            index += 1

        while index < n and s[index].isdigit():
            digit = int(s[index])

            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return  INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            index += 1
        return sign * result
#O(N)
#O(1)