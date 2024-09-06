# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        if root is None:
            return ans
        queue = collections.deque([(root)])
        while queue:
            sub_max = -float('inf')
            level_ = len(queue)
            for i in range(level_):
                curr_node = queue.popleft()
                sub_max = max(sub_max, curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            ans.append(sub_max)
        return ans

