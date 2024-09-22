"""
Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low_p = curr = 0
        high_p = len(nums) -1

        while curr <= high_p:
            if nums[curr] == 0:
                nums[low_p], nums[curr] = nums[curr], nums[low_p]
                low_p += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[high_p] = nums[high_p], nums[curr]
                high_p -= 1
            else:
                curr += 1

        # O(N)
        # O(1)