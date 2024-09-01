"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Floyd's Tortoise and Hare (Cycle Detection)
        #create 2 pointers, fast and slow
        # once they intersect, break
        #create another pointer and in that pointer and slow pointer intersect and thats the result

        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow
        #O(N)
        #O(1)

        #can be done with set but it takes O(N) space