'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(N)
        frequcy_map = defaultdict()
        bucket_array = [[] for i in range(len(nums) + 1)]
        result = []
        for i in range(len(nums)):
            frequcy_map[nums[i]] = 1 + frequcy_map.get(nums[i], 0)
        for num, val in frequcy_map.items():
            bucket_array[val].append(num)
        for i in range(len(bucket_array) - 1, 0, -1):
            if bucket_array[i] != []:
                for j in bucket_array[i]:
                    result.append(j)
                    k -= 1
            if k == 0:
                break
        return result

        """
        #O(n log k)
        freqncy_map = collections.Counter(nums)
        heap = []
        for num,freq in freqncy_map.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq,num))
            else:
                heapq.heappushpop(heap, (freq,num))
        return [x[1] for x in heap]
        """