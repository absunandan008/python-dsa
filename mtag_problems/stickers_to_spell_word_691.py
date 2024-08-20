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

        # Sort stickers by length to prioritize shorter ones (optional, but may help optimize)
        stickers.sort(key=lambda x: len(x))

        # Convert each sticker to a Counter for easy frequency calculations
        stickers = [collections.Counter(x) for x in stickers]

        # Memoization dictionary to store already computed results for target substrings
        memo = {}

        # Depth-first search function to find the minimum stickers required
        def dfs(target_str):
            # If the target string is empty, no stickers are needed
            if not target_str:
                return 0

            # If this target has already been computed, return the stored result
            if target_str in memo:
                return memo[target_str]

            # Count the frequency of each character in the target string
            target_counter = collections.Counter(target_str)
            ans = float('inf')  # Initialize the answer with infinity

            # Try to cover the target with each sticker
            for sticker in stickers:
                # If the first character of the target isn't in the sticker, skip it
                if target_str[0] not in sticker:
                    continue

                # Calculate remaining characters in the target after using the sticker
                remaining_characters = target_counter - sticker
                # Construct the next target string from the remaining characters
                next_target = "".join([char * count for char, count in remaining_characters.items()])
                # Recursively calculate the number of stickers for the remaining target
                ans = min(ans, 1 + dfs(next_target))

            # Store the computed result in the memo dictionary
            memo[target_str] = ans
            return ans

        # Call the dfs function for the entire target and handle the case of infinity
        result = dfs(target)
        return result if result != float('inf') else -1
