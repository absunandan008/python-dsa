from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            if target - nums[i] in mem:
                return [i, mem[target - nums[i]]]
            else:
                mem[nums[i]] = i

instance = Solution()
print(instance.twoSum([2,7,11,15], 9) , "|Output: [0,1]")
print(instance.twoSum([3,2,4], 6) , "|Output: [1,2]")
print(instance.twoSum([3,3], 6) , "|Output: [1,2]")
