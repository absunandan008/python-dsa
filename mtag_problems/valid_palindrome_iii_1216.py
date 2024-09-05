"""
Given a string s and an integer k, return true if s is a k-palindrome.
A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

Example 1:
Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.

Example 2:
Input: s = "abbababa", k = 1
Output: true

"""

class Solution:

    def isValidPalindrome(self, s: str, k: int) -> bool:
        self.strings = s
        if not k:
            return self.is_palindrone(0, len(s) -1)
        memo = {}

        def helper_palindrome(i,j,k):
            if ((i,j,k)) in memo:
                return memo[(i,j,k)]
            if k < 0:  # Added base case for negative k
                return False
            elif k == 0:
                memo[(i,j,k)] = self.is_palindrone(i,j)
            else:
                while i < j:
                    if self.strings[i] != self.strings[j]:
                        memo[(i,j,k)] = helper_palindrome(i+1,j,k-1) or helper_palindrome(i,j-1,k-1)
                        return memo[(i,j,k)]
                    i += 1
                    j -= 1
                memo[(i, j, k)] = True
            return memo[(i,j,k)]

        return helper_palindrome(0, len(s)-1, k)

    def is_palindrone(self, i, j):
        while i < j:
            if self.strings[i] != self.strings[j]:
                return False
            i += 1
            j -= 1
        return  True