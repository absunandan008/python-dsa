'''
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        final_cnt = 0
        def expand_from_center(lo,hi):
            sub_str = 0
            while lo>= 0 and hi < len(s) and s[lo] == s[hi]:
                sub_str += 1
                lo -= 1
                hi += 1
            return  sub_str

        for i in range(len(s)):
            # Count odd-length palindromes
            final_cnt += expand_from_center(i,i)
            # Count Even-length palindromes
            final_cnt += expand_from_center(i, i+1)
        return  final_cnt

# Test the solution
solution = Solution()
print(solution.countSubstrings("abc"))  # Output: 3
print(solution.countSubstrings("aaa"))  # Output: 6