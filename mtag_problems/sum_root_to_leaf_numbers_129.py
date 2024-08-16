"""

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        root_to_leaf = [0]

        def dfs(node, curr_num):
            if node:
                curr_num = curr_num * 10 + node.val
                if node.left is None and node.right is None:
                    root_to_leaf[0] += curr_num
                else:
                    dfs(node.left,curr_num)
                    dfs(node.right, curr_num)
        dfs(root, 0)
        return root_to_leaf[0]