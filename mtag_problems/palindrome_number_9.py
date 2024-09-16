'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        #negetive numbers are never palindrome
        if x < 0 or (x % 10 == 0 and x != 0 ):
            return False

        # get the last half of number
        reverted_number = 0
        while reverted_number < x:
            reverted_number = 10 * reverted_number + x % 10
            x //= 10

        if x == reverted_number or reverted_number//10 == x:
            return True
        else:
            return False

    #O(log to the base 10 (n))
    #O(1)