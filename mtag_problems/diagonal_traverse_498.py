"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

"""
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        r_max = len(mat)
        c_max = len(mat[0])
        result = []
        upside = True

        r_cur = c_cur = 0
        while r_cur < r_max and c_cur < c_max:
            if upside:
                while r_cur >= 0 and c_cur < c_max:
                    result.append(mat[r_cur][c_cur])
                    r_cur -= 1
                    c_cur += 1

                if c_cur == c_max:
                    r_cur += 2
                    c_cur -= 1
                else:
                    r_cur += 1
                upside = False
            else:
                while r_cur < r_max and c_cur >= 0:
                    result.append(mat[r_cur][c_cur])
                    r_cur += 1
                    c_cur -= 1

                if r_cur == r_max:
                    c_cur += 2
                    r_cur -= 1
                else:
                    c_cur += 1
                upside = True
        return result