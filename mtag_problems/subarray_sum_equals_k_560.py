'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_dict = {0: 1}
        prefix_sum = 0
        for u in range(len(nums)):
            prefix_sum += nums[u]
            if prefix_sum - k in prefix_dict:
                count += prefix_dict[ prefix_sum - k ]
            prefix_dict[prefix_sum] = 1 + prefix_dict.get(prefix_sum, 0)
        return count
#O(N) - Time
#O(N) - Space