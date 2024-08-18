"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        tmp = []
        def backtracking(index):
            if len(tmp) == k:
                result.append(tmp[:])
                return

            need = k - len(tmp)
            remain = n - index + 1
            available = remain - need
            for i in range(index, index+available+1):
                tmp.append(i)
                backtracking(i+1)
                tmp.pop()
        backtracking(1)
        return result