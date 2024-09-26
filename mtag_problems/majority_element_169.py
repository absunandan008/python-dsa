"""
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyer-Moore Voting Algorithm
        count = 0
        curr_majority = None

        for num in nums:
            if count == 0:
                curr_majority = num
            if num == curr_majority:
                count += 1
            else:
                count -= 1
        return  curr_majority

        # O(N)
        # O(1)

        """
        max_count_map = collections.Counter(nums)
        answer = nums[0]
        for key,value in max_count_map.items():
            if value > max_count_map[answer]:
                answer = key

        return answer
        """
