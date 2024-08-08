'''
Given the root node of a binary search tree
and two integers low and high,
return the sum of values of all nodes
with a value in the inclusive range [low, high].
'''
import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        output = 0
        if not root:
            return output
        queue = collections.deque([root])

        while queue:
            node = queue.pop()
            if node and low <= node.val <= high:
                output += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return output
