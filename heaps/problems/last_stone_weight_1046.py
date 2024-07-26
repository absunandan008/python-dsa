import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        #add negetive value , then we can use minheap to create a maxheap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        #till heap length is 2 or more
        while len(stones) > 1:
            # first will be like -8
            first = heapq.heappop(stones)
            # second will be like -7
            second = heapq.heappop(stones)
            if second > first:
                # -8 - (-7) = -1, which will be pushed in heap
                heapq.heappush(stones, first - second)
        # adding a zero in case heap is empty
        stones.append(0)
        return abs(stones[0])
