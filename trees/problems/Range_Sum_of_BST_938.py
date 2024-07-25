# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        output = [0]
        def dfs(node, low, high):
            if not node:
                return None
            if node.val >= low and node.val <= high:
                output[0] += node.val
            dfs(node.left, low, high)
            dfs(node.right, low, high)
        dfs(root, low, high)
        return output[0]