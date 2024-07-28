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