"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """

        basically look from opposite side. Generally if we substract prefix sum of 2 indices.
        Now here is we want if module of that step is 0 or not. We calculate prefix_mod = (prefix_mod+nums[i]) % k.
        then we search if we have seen it in hashmap or not. Hashmap mod_seen = {0: -1}.
        We keep 0th index value as -1 because we want to gave array length as 2.
        now if we find prefix_mod as key in map then return true else all that prefix mod as key and value as index
        """
        prefix_mod = 0
        mod_seen = {0: -1}
        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k
            if prefix_mod in mod_seen:
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                mod_seen[prefix_mod] = i
        return False