# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if root is None:
            return answer
        def dfs(root, level):
            if level == len(answer):
                answer.append(root.val)
            if root.right:
                dfs(root.right, level+1)
            if root.left:
                dfs(root.left, level+1)

        dfs(root, 0)
        return answer