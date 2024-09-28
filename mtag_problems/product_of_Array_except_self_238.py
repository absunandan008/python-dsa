"""
Given an integer array nums, 
return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            length = len(nums)
            
            left = [0] * length
            
            left[0] = 1
            
            for i in range(1,length):
                left[i]= nums[i-1]*left[i-1]
            
            right_prod = 1
            
            for i in range(length-1,-1,-1):
                left[i] = left[i] * right_prod
                right_prod *= nums[i]
            
            return left
            #O(N)
            #O(1)
    
    def productExceptSelf_bigspace(self, nums: List[int]) -> List[int]:
        length = len(nums)

        left = [0] * length
        right = [0] * length

        left[0] = 1
        right[-1] = 1

        for i in range(length-2,-1,-1):
            right[i] = nums[i+1] * right[i+1]
        
        for i in range(1,len(nums)):
            left[i] = nums[i-1] * left[i-1]

        ans = []
        for i in range(len(nums)):
            ans.append(left[i]*right[i])
        
        return ans
        