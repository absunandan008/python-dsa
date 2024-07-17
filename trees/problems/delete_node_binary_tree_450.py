# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, value):
        if self is None:
            self.val = value
        else:
            self._recursive_insert(self, value)

    def _recursive_insert(self, node, value):
        if node.val < value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._recursive_insert(node.right, value)
        elif node.val > value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._recursive_insert(node.left, value)

    def print_tree(self):
        def _print_recursive(node, level=0, prefix="Root:"):
            if node is not None:
                print(" " * (level * 4) + prefix + str(node.val))
                _print_recursive(node.left, level + 1, "L---")
                _print_recursive(node.right, level + 1, "R---")

        _print_recursive(self)


    def deleteNode(self, root, key: int):
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode(root.right, root.val)
        return root





# Example usage
tree = TreeNode()

# Insert nodes
nodes_to_insert = [5, 3, 7, 2, 4, 6, 8]
for node in nodes_to_insert:
    tree.insert(node)

print("Initial tree:")
tree.print_tree()

tree.deleteNode(tree, 3)

print("Deleted  tree:")
tree.print_tree()