"""
Given a sorted integer array arr, two integers k and x,
return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
"""


class Solution:
    def findClosestElementsNonOptimal(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-abs(arr[i] - x), arr[i]))

        for j in range(k, len(arr)):
            if (-abs(arr[j] - x)) > heap[0][0]:
                heapq.heappushpop(heap, (-abs(arr[j] - x), arr[j]))
        heap.sort(key=lambda x: x[1])
        return [x for _, x in heap]