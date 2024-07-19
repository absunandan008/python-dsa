# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if root is None:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            res[0] = max(res[0], left + right)
            return 1 + max(left, right)

        dfs(root)
        return res[0]