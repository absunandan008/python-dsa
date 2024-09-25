"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len =len(needle)
        haystack_len = len(haystack)

        for win_start in range(haystack_len-needle_len+1):
            for i in range(needle_len):
                if needle[i] != haystack[win_start+i]:
                    break
                if i == needle_len -1:
                    return win_start
        return -1
        #O(n*m)
        #O(1)