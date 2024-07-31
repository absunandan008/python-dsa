import re


class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Implementation of the data method goes here
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] != s[end]:
                return self.isPalindrome(s[start:end]) or self.isPalindrome(s[start:end+1])
            start += 1
            end -= 1
        return True

    def isPalindrome(self, s: str) -> bool:
        s= "".join(char.lower() for char in s if char.isalnum())
        start = 0
        end = len(s)-1

        while start<end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
# Create an instance of the Solution class
a = Solution()
abc = "abccdba"
print("valid data for: race a car:", a.isPalindrome("race a car"))
# Call the data method on the instance
print("valid data for "+ abc, a.validPalindrome(abc))