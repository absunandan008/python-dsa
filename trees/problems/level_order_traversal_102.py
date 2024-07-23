# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Initialize Output
        output = []
        if root is None:
            return output
        #Add root in queue
        queue = deque[root]
        while queue:
            #We will need to find the numbers of nodes on each level
            level_size = len(queue)
            level_output = []

            for level_travese in range(level_size):
                node = queue.popleft()
                level_output.append(node.val)
                #for each node of level, check if there is anything left or right and then add it in queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(level_output)
        return output

