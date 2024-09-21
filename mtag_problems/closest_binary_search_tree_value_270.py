"""
Given the root of a binary search tree and a target value,
return the value in the BST that is closest to the target.
If there are multiple answers, print the smallest.
Example 1:
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:
Input: root = [1], target = 4.428571
Output: 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val

        while root:
            # Calculate the differences for root.val and closest
            curr_diff = abs(root.val-target)
            closest_diff = abs(closest-target)

            # If root.val is closer to target, update closest
            if curr_diff < closest_diff:
                closest = root.val
            elif curr_diff == closest_diff:
                # If distances are equal, choose the smaller value
                closest = min(closest, root.val)

            # Determine the direction to traverse
            root = root.left if target < root.val else root.right

        return  closest
