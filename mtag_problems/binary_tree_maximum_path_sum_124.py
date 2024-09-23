"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""
import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Idea is to do dfs but do not include if depth is negetive
        # max(kadane_algo(node.left), 0) or max(kadane_algo(node.right), 0)
        # Basically you are calculating diameter with node value added
        # then while returning either side of the path because we are trying to find max at each return

        max_sum = -math.inf
        def kadane_algo(node):
            nonlocal max_sum
            if not node:
                return 0

            #We do not want negetive values ever
            left_max = max(kadane_algo(node.left), 0)
            right_max = max(kadane_algo(node.right), 0)

            max_sum = max(max_sum, left_max+right_max+node.val)

            return max(left_max+node.val, right_max+node.val)

        kadane_algo(root)
        return max_sum