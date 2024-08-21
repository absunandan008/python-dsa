import heapq
import random

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #quickselect
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [],[],[]
            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return quick_select(left, k)
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            return pivot
        return quick_select(nums, k)

    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        nums =  nums
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
