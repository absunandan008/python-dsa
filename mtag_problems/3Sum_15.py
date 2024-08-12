'''
Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array
        #go through one element at a time
        #if current element is equal to last element then continue except if current element is first one
        #then 2 pointer approach, calculate lo and hi
        # while lo < hi, calculate sum equal to nums[i] + nums[lo] + nums[hi]
        # if sum == 0, add it to result set else if sum > 0 then reduce hi by 1 else increase lo by 1
        # sum = 0, while lo < hi and also lo[i] == lo[i-1], increase lo by 1
        nums.sort()
        output = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo = i+1
            hi = len(nums) - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums [hi]
                if sum == 0:
                    output.append([nums[i],nums[lo],nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo +=1
                elif sum > 0:
                    hi -= 1
                else:
                    lo += 1
        return output

