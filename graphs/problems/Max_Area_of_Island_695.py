from typing import List


class Solution:
    def maxAreaOfIsland_firstImpl(self, grid: List[List[int]]) -> int:

        Rows, Cols = len(grid), len(grid[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def find_area(grid, cur_row, cur_col):
            if 0 <= cur_col < Cols and 0 <= cur_row < Rows and grid[cur_row][cur_col] == 0:
                grid[cur_row][cur_col] = 0
                area = 1

                for row,col in directions:
                    area += find_area(grid,cur_row+row, cur_col+col)
                return area
            else:
                return 0

        max_area = 0
        for row in range(Rows):
            for col in range(Cols):
                max_area = max(max_area, find_area(grid, row, col))
        return max_area

    #dfs impl
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] == 0 or (row, col) in visited:
                return 0

            visited.add((row, col))
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                max_area = max(max_area, dfs(row, col))
        return max_area

    # dfs without set
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] == 0:
                return 0

            grid[row][col] = 0  # Mark as visited by changing to 0
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                max_area = max(max_area, dfs(row, col))
        return max_area