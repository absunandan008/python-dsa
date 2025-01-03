"""
Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

import math
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = math.inf
        n = len(nums)
        
        nums.sort()
        
        for i in range(n-2):
            lo = i+1
            hi = n-1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target-sum) < abs(diff):
                    diff = target-sum
                if sum > target:
                    hi -= 1
                else:
                    lo += 1
                    
            if diff == 0:
                break
        
        return target-diff
        #O(n^2)
        #O(1)