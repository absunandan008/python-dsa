"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.'
both indicate a queen and an empty space, respectively.
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        empty_board = [["."] * n for _ in range(n)]

        # to create board
        def creat_board(slate):
            board = []
            for row in slate:
                board.append("".join(row))
            return board

        def backtracking(row, diagonals, anti_diagonals, cols, slate):
            if row == n:
                ans.append(creat_board(slate))
                return

            for col in range(n):
                cur_diagonal = row - col
                cur_anti_diagonal = row + col

                if (
                        col in cols
                        or cur_diagonal in diagonals
                        or cur_anti_diagonal in anti_diagonals
                ):
                    continue

                # add queen to board
                cols.add(col)
                diagonals.add(cur_diagonal)
                anti_diagonals.add(cur_anti_diagonal)
                slate[row][col] = "Q"

                backtracking(row + 1, diagonals, anti_diagonals, cols, slate)

                # remove
                cols.remove(col)
                diagonals.remove(cur_diagonal)
                anti_diagonals.remove(cur_anti_diagonal)
                slate[row][col] = "."

        backtracking(0, set(), set(), set(), empty_board)
        return ans
