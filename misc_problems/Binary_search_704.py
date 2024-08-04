from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = ( left + right ) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return -1

    def recusiveSearch(self, nums: List[int], target: int) -> int:
        def helper(nums: List[int], target: int, left: int, right: int):
            if left > right:
                return -1
            middle = (right+left)//2
            if target < nums[middle] :
                return helper(nums,target,left,middle-1)
            if target > nums[middle] :
                return helper(nums, target, middle+1, right)
            return middle
        return helper(nums,target,0, len(nums) - 1)



#
arr = [-1,0,3,5,9,12]
solution = Solution()
##print("Binaty Search: ", solution.search(arr, 5))
print("Binaty Search recursive: ", solution.recusiveSearch(arr, 9))