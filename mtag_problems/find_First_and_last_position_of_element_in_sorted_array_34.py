"""
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    #basically Bound Binary search or double binary search
    #So we do bin search first and if leftbias is true, assing current mid as right and then do search again
    #else we asing mid+1 to left and do search again, First one is left bound and later one is right bound
    #Call method twice wiht one left and one right and return
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.bound_bin_search(nums,target,True),self.bound_bin_search(nums,target,False)]
    def bound_bin_search(self, nums, target, left_b):
        i = -1
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = lo + (hi-lo)//2

            if nums[mid] == target:
                i = mid
                if left_b:
                    hi = mid
                else:
                    lo = mid+1
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return i