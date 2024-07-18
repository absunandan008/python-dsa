# Definition for a binary tree node.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)
        return 1 + max(ldepth, rdepth)

    def max_depth_with_stack(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = ([root, 1])
        max_depth = 1

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth+1))