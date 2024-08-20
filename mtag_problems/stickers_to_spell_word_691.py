"""
We are given n different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given string target by cutting individual letters from your
collection of stickers and rearranging them. You can use each sticker more than once if you want,
and you have infinite quantities of each sticker.

Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

Note: In all test cases, all words were chosen randomly from the 1000 most common US English words,
and target was chosen as a concatenation of two random words.
"""
import collections
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:

        #freuqency map to get counts of each string in stickets
        #also use memoization.
        #Logic is to go through letter and each time check if first letter of string is equal to some sticker
        #if it is then substract frequency of target string(we will need to create this one) and sticker and then dfs again next time.after we come
        #out of dfs, add answer to memoization
        sticker_freq = [collections.Counter(x) for x in stickers]

        #memoization
        memo = {}

        #dfs
        def dfs(target_str):
            if not target_str:
                return 0

            if target_str in memo:
                return memo[target_str]

            ans = float('inf')
            target_counter = collections.Counter(target_str)
            for sticker in sticker_freq:
                if target_str[0] not in sticker:
                    continue

                remaining_str = target_counter - sticker
                new_target = "".join([char * count for char,count in remaining_str.items()])
                ans = min(ans, 1+ dfs(new_target))

            memo[target_str] = ans
            return ans

        final_ans = dfs(target)
        return final_ans if final_ans != float('inf') else -1
