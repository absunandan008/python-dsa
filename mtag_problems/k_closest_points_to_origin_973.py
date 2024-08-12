import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(k):
            dist = -self.ecud_distance(points[i])
            heap.append((dist, i))
        heapq.heapify(heap)

        for i in range(k, len(points)):
            dist = -self.ecud_distance(points[i])
            if dist > heap[0][0]:
                heapq.heappushpop(heap, (dist, i))
        result = []
        for _, i in heap:
            result.append(points[i])
        return result


    def ecud_distance(self, point):
        return point[0] ** 2 + point[1] ** 2