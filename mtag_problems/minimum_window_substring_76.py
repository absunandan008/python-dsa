"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window.
 If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        This function finds the smallest window in the string `s` that contains all characters of the string `t`.

        To achieve this, we use a sliding window approach with two frequency maps:
        1. `target_map`: A frequency map prepopulated with the required frequencies of characters in `t`.
        2. `window_map`: A frequency map that we populate dynamically as we expand the window over `s`.

        We also use two pointers, `l` and `r`, to represent the left and right boundaries of the window, respectively.

        - `required`: The number of unique characters in `t` that need to be fully matched in the window.
        - `match`: A counter to keep track of how many unique characters in `s` currently match the required frequency from `t`.

        The outer loop expands the window by moving the `r` pointer to the right. For each character in `s[r]`, we update `window_map`.
        If the current character's frequency in `window_map` matches its frequency in `target_map`, we increment `match`.

        Whenever `match` equals `required`, it means our window contains all characters from `t` with the correct frequencies.
        We then enter an inner while loop to contract the window by moving the `l` pointer to the right as much as possible while still satisfying the condition `match == required`.

        During this contraction, we check if the current window is the smallest valid window found so far. If it is, we update our result.

        After contracting, we decrement the frequency of the character at `s[l]` in `window_map`. If this causes a mismatch (i.e., the frequency in `window_map` drops below the frequency in `target_map`), we decrement `match` and continue contracting.

        Finally, if we find a valid window, we return it; otherwise, return an empty string.
        """
        if not s or not t or len(t) > len(s):
            return ""

        target_map = collections.Counter(t)
        window_map = collections.defaultdict(int)
        required = len(target_map)
        match = l = r = 0

        ans = (float('inf'), 0, 0)

        while r < len(s):
            cur_char = s[r]
            window_map[cur_char] += 1

            if cur_char in target_map and window_map[cur_char] == target_map[cur_char]:
                match += 1

            while l <= r and required == match:
                to_remove = s[l]

                if (r - l + 1) < ans[0]:
                    ans = (r - l + 1, l, r)

                window_map[to_remove] -= 1
                if to_remove in target_map and window_map[to_remove] < target_map[to_remove]:
                    match -= 1
                l += 1
            r += 1

        return s[ans[1]:ans[2] + 1] if ans[0] != float('inf') else ""


