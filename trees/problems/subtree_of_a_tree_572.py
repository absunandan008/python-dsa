# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        #Try to find if this tree node is equal to a subtree node
        if self.isSameTree(root, subRoot):
            return True
        #if the tree node is not equal to subtree and then either move left or right
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    #find if these are same tree or not
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)