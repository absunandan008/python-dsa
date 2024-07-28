from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        Rows, Cols = len(heights), len(heights[0])

        atl, pac = set(), set()

        def dfs(rows, cols, visited, height):
            if rows < 0 or rows == Rows or cols < 0 or cols == Cols or (rows,cols) in visited or heights[rows][cols] < height:
                return
            visited.add((rows,cols))
            dfs(rows+1,cols,visited,heights[rows][cols])
            dfs(rows-1,cols,visited,heights[rows][cols])
            dfs(rows,cols-1,visited,heights[rows][cols])
            dfs(rows,cols+1,visited,heights[rows][cols])

        for c in range(Cols):
            dfs(0,c,pac,heights[0][c])
            dfs(Rows-1, c, atl, heights[Rows-1][c])

        for r in range(Rows):
            dfs(r,0,pac, heights[r][0])
            dfs(r, Cols-1, atl, heights[r][Cols-1])

        ##return list(atl.intersection(pac))
        output = []
        for row in range(Rows):
            for col in range(Cols):
                if (row,col) in atl and (row,col) in pac:
                     output.append([row,col])
        return output