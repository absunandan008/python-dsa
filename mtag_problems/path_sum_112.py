# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum - root.val)]

        while stack:
            node, sum = stack.pop()
            if not node.left and not node.right and sum == 0:
                return True
            if node.left:
                stack.append((node.left, sum - node.left.val))

            if node.right:
                stack.append((node.right, sum - node.right.val))

        return False

        """
        if not root:
            return False

        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        """
