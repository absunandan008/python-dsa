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
            #goto right and left
            left, right = dfs(root.left), dfs(root.right)
            #check if current max diameter is greater then left+right , if yes then set it to result
            res[0] = max(res[0], left + right)
            #calculating the height each time
            return 1 + max(left, right)

        dfs(root)
        return res[0]