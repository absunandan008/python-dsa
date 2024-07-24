# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        count = [0]
        def dfs(root, val):
            if root is None:
                return 0

            if root.val >= val:
                count[0] = count[0] + 1
                val = max(val,root.val)
            dfs(root.left,val)
            dfs(root.right,val)
            return root, val
        dfs(root,root.val)
        return count[0]
