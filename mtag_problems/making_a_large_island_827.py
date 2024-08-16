from typing import List


class Solution:
    """
    Think about assigning an index to each island. Like if u visit first island then assin it 2
    and next set of islands assign it 3,. Create a Map and save the number of 1's in each island group
    like lets say 2 index has 3 one's then its area is 3 which means index[2] = 3,
    lets next group of 1's has area 3, means index[3] = 3. Not again loop through grid and for each 0,
    find area of all 4 adjacent using the index area map. sum all of those. now if 0's sum or 1's sum whichever is greater ,
    retrun it, use DFS and have a visit set inside dfs and assin those visited grid with the current index
    """
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        def dfs(r, c, index):
            seen = {(r, c)}
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                grid[r][c] = index
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)):
                    if (nr, nc) not in seen and 0 <= nr < N and 0 <= nc < N and grid[nr][nc]:
                        stack.append((nr, nc))
                        seen.add((nr, nc))
            return len(seen)

        area = {}
        index = 2
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    area[index] = dfs(x, y, index)
                    index += 1
        result = max(area.values() or [0])
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    seen = set()
                    for nr, nc in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])
                    sum_adjacent = 0
                    for i in seen:
                        sum_adjacent += area[i]
                    result = max(result, 1 + sum_adjacent)
        return result

        '''
        ans = 0
        has_zero = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    has_zero = True
                    grid[x][y] = 1
                    ans = max(ans,dfs(x,y))
                    grid[x][y] = 0
        return ans if has_zero else N*N
        '''



