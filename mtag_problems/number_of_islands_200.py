from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        self.maxrow = len(grid)
        self.maxcol = len(grid[0])
        islands = 0
        for r in range(self.maxrow):
            for c in range(self.maxcol):
                if grid[r][c] == "1":
                    islands += 1
                    self.dfs(grid, r , c)
        return islands

    def dfs(self, grid, r, c):
        if r < 0 or r >= self.maxrow or c < 0 or c >= self.maxcol or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        self.dfs(grid,r-1,c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)