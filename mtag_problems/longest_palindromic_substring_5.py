"""
Given a string s, return the longest
palindromic

substring
 in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len = 0
        res_out = ""

        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_len = r - l + 1
                    res_out = s[l:r + 1]
                l -= 1
                r += 1

            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_len = r - l + 1
                    res_out = s[l:r + 1]
                l -= 1
                r += 1

        return res_out