'''
There are n buildings in a line. You are given an integer array heights of size n
that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view
if the building can see the ocean without obstructions.
Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
'''
from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        lengthofStack = len(heights)
        stack = []

        for u in range(lengthofStack):
            while stack and heights[stack[-1]] <= heights[u]:
                stack.pop()
            stack.append(u)
        return stack