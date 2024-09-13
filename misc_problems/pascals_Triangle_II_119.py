'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
'''
from typing import List


class Solution:
    #initiate memo
    cache = {}
    def getNum(self, row, col):
        if (row,col) in self.cache:
            return self.cache[(row,col)]

        if row == 0 or col == 0 or row == col:
            self.cache[(row,col)] = 1
            return 1

        self.cache[(row,col)] = self.getNum(row-1,col-1) + self.getNum(row-1,col)
        return self.cache[(row,col)]

    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex+1):
            ans.append(self.getNum(rowIndex, i))
        return ans
