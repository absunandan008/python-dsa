"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array
if you can flip at most k 0's.
"""
from typing import List

# so basic idea is sliding window but within the window there can only be K zeros
# so we increae right with the loop
#if we ever find a 0 we increase a variable called size
# everytime when size is greater than k, which means we have more zeros in window than needed
#till size is greater then zero, if nums[left] == 0, reduce size by one but
#keep sliding left till we reach a point where size is not greater than k
#each iteration find max = max(max, right-left+1)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lo = 0
        longest = 0
        size = 0
        for hi in range(len(nums)):
            if nums[hi] == 0:
                size += 1

            while size > k:
                if nums[lo] == 0:
                    size -= 1
                lo += 1

            longest = max(longest, hi-lo+1)
        return longest
