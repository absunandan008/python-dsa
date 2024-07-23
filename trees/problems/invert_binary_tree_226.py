# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, value):
        if self is None:
            self,val = value
        else:
            self._recursive_insert(self,value)

    def print_tree(self):
        def _print_recursive(node, level=0, prefix="Root:"):
            if node is not None:
                print(" " * (level * 4) + prefix + str(node.val))
                _print_recursive(node.left, level + 1, "L---")
                _print_recursive(node.right, level + 1, "R---")

        _print_recursive(self)

    def _recursive_insert(self,node,value):
        if value < node.val:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._recursive_insert(node.left,value)
        elif value > node.val:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._recursive_insert(node.right,value)
    def invertTree_NotOptimal(self, root):
        #NonOptimal solution. Go through tree and then swap the left and right nodes
        if root is None:
            return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        #Now we exchange the nodes
        dummy = root.left
        root.left = root.right
        root.right = dummy

        return root

    def invert_tree_optimal(self, root):
        if root is None:
            return root

        root.left, root.right = self.invert_tree_optimal(root.right), self.invert_tree_optimal(root.left)
        return root


if __name__ == "__main__":
    # Example usage
    tree = TreeNode()

    # Insert nodes
    nodes_to_insert = [5, 3, 7, 2, 4, 6, 8]
    for node in nodes_to_insert:
        tree.insert(node)

    print("Initial tree:")
    tree.print_tree()

    #tree.invertTree_NotOptimal(tree)
    tree.invert_tree_optimal(tree)

    print("Inverted  tree:")
    tree.print_tree()