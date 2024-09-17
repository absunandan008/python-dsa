"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""


class Solution:
    def reverse(self, x: int) -> int:
        max_int = (2 ** 31) - 1
        # min_int = -(2 ** 31)
        ans = 0
        sign = 1
        if x < 0:
            x = -1 * x
            sign = -1

        while x != 0:
            ans = ans * 10 + (x % 10)
            x //= 10
            if ans > max_int:
                return 0

        return sign * ans
    # O(Log10x)
    # O(1)



