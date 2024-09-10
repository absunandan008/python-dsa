"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = [0] * (n+1)
        return self.climb_stairs(0, n)

    def climb_stairs(self, index, n):
        if index > n:
            return 0
        if index == n:
            return 1
        if self.memo[index] > 0:
            return self.memo[index]
        self.memo[index] = self.climb_stairs(index+1, n) + self.climb_stairs(index+2, n)
        return self.memo[index]
#O(N)
#O(N)
