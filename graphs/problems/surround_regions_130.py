from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # how the algo works.
        # We start in border on all 4 sides and do dfs to inside.
        # if we find a O on border then DFS from there to where it ends
        # and those are unsurrounded regions. Mark it as T
        # then Run through whole matrix again and mark all the left over
        # O's as X
        # then run again and mark T's as O's.
        # Nothing to return

        ROWS, COLS = len(board), len(board[0])

        #define DFS and assign border O's to T's
        def dfs(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        #go through border rows which have O's and convert O's to T's
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row in [0, ROWS-1] or col in [0, COLS-1]):
                    dfs(row, col)

        # go through all and convert O's to X's
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
        # go through all and convert O's to X's
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "T":
                    board[row][col] = "O"