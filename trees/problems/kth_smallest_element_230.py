# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        result = []
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            self.k -= 1
            if self.k == 0:
                result.append(root.val)
            dfs(root.right)
            return root
        dfs(root)
        return result[0]