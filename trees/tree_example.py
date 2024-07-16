class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)

        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def delete(self, value):
        self.root = self._delete_recursively(self.root, value)

    def _delete_recursively(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursively(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursively(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

        min_node = self._find_min(node.right)
        node.value = min_node.value
        node.right = self._delete_recursively(node.right, min_node.value)

        return node

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right,result)

    def print_tree(self):
        def _print_recursive(node, level=0, prefix="Root:"):
            if node is not None:
                print(" " * ( level * 4 ) + prefix + str(node.value))
                _print_recursive(node.left, level + 1, "L---")
                _print_recursive(node.right, level + 1 , "R---")
        _print_recursive(self.root)



#example usage
tree = BinaryTree()

# Insert Nodes
nodes_to_insert = [5, 3, 7, 2, 4, 6, 8]
for node in nodes_to_insert:
    tree.insert(node)

#print initial tree
tree.print_tree()

##Print in order
print("\nInorder traversal:", tree.inorder_traversal())

print("---------Now Deleting a node-------")
##Delete 3
tree.delete(3)

print("\nTree after deleting 3:")
tree.print_tree()

print("\nInorder traversal after deletion:", tree.inorder_traversal())
