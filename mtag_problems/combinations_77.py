"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sub_res = []

        def backtracking(index):
            if len(sub_res) == k:
                res.append(sub_res[:])
                return
            need = k - len(sub_res)
            remain = n - index + 1
            available = remain - need
            for i in range(index, index + available + 1):
                # for i in range(index, n+1):
                sub_res.append(i)
                backtracking(i + 1)
                sub_res.pop()

        backtracking(1)
        return res