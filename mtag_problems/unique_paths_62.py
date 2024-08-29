"""

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_grid = [[1] * n for _ in range(m)]

        for row in range(1,m):
            for col in range(1,n):
                dp_grid[row][col] = dp_grid[row-1][col] + dp_grid[row][col-1]
        return dp_grid[m-1][n-1]

    def uniquePathsBruteForece(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePathsBruteForece(m-1,n) + self.uniquePathsBruteForece(m,n-1)