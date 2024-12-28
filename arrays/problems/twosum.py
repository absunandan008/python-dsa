from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        #Enumerate gives indice and value both
        for i,num in enumerate(nums):
            if target-num in mem:
                return [mem[target-num], i]
            mem[num] = i
        return []

instance = Solution()
print(instance.twoSum([2,7,11,15], 9) , "|Output: [0,1]")
print(instance.twoSum([3,2,4], 6) , "|Output: [1,2]")
print(instance.twoSum([3,3], 6) , "|Output: [0,1]")
