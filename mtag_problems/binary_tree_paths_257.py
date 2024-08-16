"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        path_to_leaf = []

        def dfs(node, curr_path):
            if node:
                curr_path += str(node.val)
                if node.right is None and node.left is None:
                    path_to_leaf.append(curr_path)
                else:
                    curr_path += "->"
                    dfs(node.left, curr_path)
                    dfs(node.right, curr_path)
        dfs(root, "")
        return path_to_leaf