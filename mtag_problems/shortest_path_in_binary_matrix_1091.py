import collections
from typing import List, Tuple

from mtag_problems.simplify_path_71 import solution


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

    def shortestPathBinaryMatrixwithPath(self, grid: List[List[int]]) -> Tuple[int, List[Tuple[int, int]]]:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1, []  # No path if start or end is blocked

        # The queue stores tuples of (row, col, path_length, path)
        queue = collections.deque([(0, 0, 1, [(0, 0)])])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        visited = set((0, 0))

        while queue:
            row, col, path_length, path = queue.popleft()

            if (row, col) == (max_row, max_col):
                return path_length, path

            for r, c in directions:
                next_row, next_col = row + r, col + c
                if 0 <= next_row <= max_row and 0 <= next_col <= max_col and (next_row, next_col) not in visited and \
                        grid[next_row][next_col] == 0:
                    new_path = path + [(next_row, next_col)]
                    queue.append((next_row, next_col, path_length + 1, new_path))
                    visited.add((next_row, next_col))

        return -1, []  # Return -1 and empty path if no path is found


s = Solution()
binary_matrix = [[0,0,0],[1,1,0],[1,1,0]]

print(s.shortestPathBinaryMatrixwithPath(binary_matrix))