"""
Given an integer array nums, find the
subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""
import math
from typing import List


class Solution:
    def maxSubArrayDividenConquer(self, nums: List[int]) -> int:

        def findBestArray(nums, left, right):
            #if its empty then return max infinity
            if left > right:
                return -math.inf

            mid = (left+right)//2
            curr = left_best_sum = right_best_sum = 0

            #find left_best_sum
            for i in range(mid-1, left-1, -1):
                curr += nums[i]
                left_best_sum = max(left_best_sum, curr)

            #reset
            curr = 0
            #find right best sum
            for i in range(mid+1, right+1):
                curr += nums[i]
                right_best_sum = max(right_best_sum, curr)

            best_sum = left_best_sum + right_best_sum + nums[mid]

            left_half =  findBestArray(nums, left, mid-1)
            right_half = findBestArray(nums, mid+1, right)

            return max(best_sum, left_half, right_half)
        return  findBestArray(nums, 0 , len(nums)-1)
    #O(N log N)
    # O(log N)


    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum = max(0,curr_sum) + num
            max_sum = max(curr_sum,max_sum)

        return  max_sum
        # O(N)
        # O(1)