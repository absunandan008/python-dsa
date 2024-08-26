"""

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        r_max = [0] * n
        l_max = [0] * n
        l_wall = 0
        r_wall = 0
        for i in range(n):
            j = -i-1
            l_max[i] = l_wall
            r_max[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
        ans = 0
        for i in range(n):
            possible = min(l_max[i], r_max[i])
            ans += max(0, possible-height[i])

        return ans

    """
    #BruteForce
    ans = 0
    size = len(height)
    for i in range(1,size-1):
        left_max = 0
        right_max = 0
        #find left max
        for j in range(i, -1, -1):
            left_max = max(left_max, height[j])
        #find right max
        for j in range(i, size):
            right_max = max(right_max, height[j])
        ans += min(left_max,right_max) - height[i]
    return ans
    # O(N^2), O(1)
    """