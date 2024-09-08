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
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # We only need k element, so substract k from end of length
        lo = 0
        hi = len(arr) - k

        while lo < hi:
            mid  = lo + (hi-lo)//2

            # not see is mid number is near to x or mid+k index number is near to k
            # if mid is near to k then move hi to mid else move lo to mid+1
            if x - arr[mid] > arr[mid+k] - x:
                # so mid+k is near to x
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo+k]
        # O(log(N-k)) for search and k to build the array = O(log(N-k) + k)
        #Space = O(1)

    def findClosestElementsNonOptimal(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-abs(arr[i] - x), arr[i]))

        for j in range(k, len(arr)):
            if (-abs(arr[j] - x)) > heap[0][0]:
                heapq.heappushpop(heap, (-abs(arr[j] - x), arr[j]))
        heap.sort(key=lambda x: x[1])
        return [x for _, x in heap]