# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root is None:
            return output

        queue = collections.deque([root])
        while queue:
            level_length = len(queue)
            for level in range(level_length):
                node = queue.popleft()
                if level == level_length - 1:
                    output.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)