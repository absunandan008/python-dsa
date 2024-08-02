# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        columnTable = {}
        result = []
        if root is None:
            return result
        # Root has 0 column index
        queue = collections.deque([(root, 0)])
        while queue:
            node, column = queue.popleft()
            if node:
                if column not in columnTable:
                    columnTable[column] = []
                columnTable[column].append(node.val)
                if node.left:
                    queue.append((node.left, column-1))
                if node.right:
                    queue.append((node.right, column+1))

        for x in sorted(columnTable.keys()):
            result.append(columnTable[x])

        return result

    ##
    # Example usage
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

result = Solution().verticalOrder(root)
print("result:",result)  # Output: [[9], [3, 15], [20], [7]]