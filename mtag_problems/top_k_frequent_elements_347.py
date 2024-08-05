'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyData = {}
        for n in nums:
            frequencyData[n] = 1 + frequencyData.get(n, 0)
        heap =  []
        for key,value in frequencyData.items():
            if len(heap) < k:
                heapq.heappush(heap, (value,key))
            else:
                heapq.heappushpop(heap, (value,key))

        return [h[1] for h in heap]