
"""
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        sol = []
        def backtracking_dfs(i):
            if i >= len(nums):
                result.append(sol.copy())
                return
            #decision to include the nums of i
            backtracking_dfs(i + 1)
            sol.append(nums[i])


            #decision not to include nums[i]
            backtracking_dfs(i + 1)
            sol.pop()

        backtracking_dfs(0)
        return result
    #Time O(2**N)
    #space O(N)

    def subsetsIteravtive(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for num in nums:
            new_subset = []
            for curr in subsets:
                tmp = curr + [num]
                new_subset.append(tmp)
            subsets += new_subset
        return subsets

    def subsetsBitManipulation(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = []

        for i in range(1<<n):
            sub_result = []
            for j in range(n):
                if i & (1<<j):
                    sub_result.append(nums[j])
            subset.append(sub_result)
        return subset

    def subsets_simplebacktracking(self, nums: List[int]) -> List[List[int]]:
        answers = []
        def backtracking(index,path):
            answers.append(path.copy())

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtracking(i+1,path)
                path.pop()

        backtracking(0, [])
        return answers



s = Solution()
# nums = [1,2,2]
# print(s.subsets([1, 2, 3]))
nums = [1,2]
print( s.subsets(nums) )

