from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        out = []
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start+1,end+1]
            if numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1