from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rowLength, colLength = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or row == rowLength or col < 0 or col == colLength or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        max = 0
        for row in range(rowLength):
            for col in range(colLength):
                if grid[row][col] == "1":
                    max += 1
                    dfs(row, col)
        return max


    def numIslandsQueue(self, grid: List[List[str]]) -> int:

        rowLength, colLength = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or row == rowLength or col < 0 or col == colLength or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        max = 0
        for row in range(rowLength):
            for col in range(colLength):
                if grid[row][col] == "1":
                    max += 1
                    dfs(row, col)
        return max
