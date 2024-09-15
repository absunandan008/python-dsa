"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
"""
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        basically we compare upper left grid in matrix. that
        means we are comparing the diagonal components
        """
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        for r in range(rows):
            for c in range(cols):
                if r > 0 and c > 0:
                    if matrix[r][c] != matrix[r-1][c-1]:
                        return False
        return True


    def isToeplitzMatrixNotOptimal(self, matrix: List[List[int]]) -> bool:
        """
        basically r-c is the diagonal and it what we save in map
        for future r-c , its matric value should be equal to the value in map
        because same diagonals have same r-c coordinates
        """
        groups = {}

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r-c not in groups:
                    groups[r-c] = matrix[r][c]
                elif groups[r-c] != matrix[r][c]:
                    return False
        return True
        #O(M*N)
        #O(M+N)