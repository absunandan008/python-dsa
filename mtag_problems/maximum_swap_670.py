"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        convert num into string
        got through it and stop as soon as you find the first one greater then last one
        else send then whole number back
        now try to find largest and set it max and max id by going right from the first one
        then start from left and as soon as you find something less than max till i+1, stop and replace and return

        """
        s = list(str(num))
        n = len(s)
        for i in range(n - 1):
            if s[i] < s[i+1]:
                break
        else:
            return num
        max_id, max_val = i+1, s[i+1]

        for j in range(i+1, n):
            if max_val <= s[j]:
                max_id, max_val = j, s[j]
        left_id = 0
        for j in range(i+1):
            if s[j] < max_val:
                left_id = j
                break

        s[max_id], s[left_id] = s[left_id], s[max_id]

        return int("".join(s[:]))

    def maximumSwapBruteForce(self, num: int) -> int:
        """
        Bruteforce
        conver nums in a list of strings
        Go through double loop and do a swap and save in a max.
        return int("".join.(max))
        """
        s = list(str(num))
        ans = s[:]
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                s[i], s[j] = s[j], s[i]
                if ans < s[:]:
                    ans = s[:]
                s[j], s[i] = s[i], s[j]
        return int("".join(ans))