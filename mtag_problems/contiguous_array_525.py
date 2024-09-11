'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

'''

"""
This function finds the maximum length of a contiguous subarray with an equal number of 0s and 1s in a binary array.
The algorithm uses a 'count' variable to keep track of the difference between the number of 1s and 0s encountered.
It increments the count for 1s and decrements for 0s. A hash map (count_dict) is used to store the first occurrence
of each count value. The key insight is that if we encounter the same count twice, the subarray between these two
indices must have an equal number of 0s and 1s. We initialize count_dict with {0: -1} to handle the case where a
valid subarray starts from the beginning of the array. As we iterate through the array, we update the max_length
whenever we find a longer valid subarray, either when the count becomes 0 (valid subarray from the start) or when
we encounter a count we've seen before (valid subarray between the current index and the previous occurrence of this count).
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        count_size = {0: -1}

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count == 0:
                max_length = i + 1
            elif count in count_size:
                max_length = max(max_length, i - count_size[count])
            else:
                count_size[count] = i

        return max_length