import collections
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_r = len(grid) - 1
        max_c = len(grid[0]) - 1

        if grid[0][0] != 0 or grid[max_r][max_c] != 0:
            return -1
        ## 0,0 for grid and 1 for distance
        queue = collections.deque([(0,0,1)])
        visited = {(0, 0)}
        directions = [(0,1),(0,-1),(1,0),(-1,0), (-1,1),(1,1),(1,-1),(-1,-1)]

        while queue:
            cur_row, cur_col, distance = queue.popleft()

            if (cur_row,cur_col) == (max_r,max_c):
                return distance
            for dir_row,dir_col in directions:
                next_row, next_col = cur_row+dir_row, cur_col+ dir_col
                if 0<= next_row <= max_r and 0<= next_col <= max_c and (next_row, next_col) not in visited and grid[next_row][next_col] == 0:
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col, distance+1))
        return -1