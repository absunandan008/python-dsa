# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #if u reach the last then return None becuase u did not find the nore
        if not root:
            return None
        # you found either p or q and now recursion will come back
        if root == p or root == q:
            return root
        # now we know p or q , it will be both on left or both on right or one in left and one in left
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        #
        if l and r:
            return root
        else:
            return l or r

    def lowestCommonAncestorBFS(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or p is None or q is None:
            return None

        parent_dict = {}
        value_to_node = {}
        parent_dict[root.val] = None
        value_to_node[root.val] = root
        queue = collections.deque([root])

        # BFS to build parent dictionary
        while queue and (p.val not in parent_dict or q.val not in parent_dict):
            node = queue.popleft()

            if node.left:
                parent_dict[node.left.val] = node.val
                value_to_node[node.left.val] = node.left
                queue.append(node.left)
            if node.right:
                parent_dict[node.right.val] = node.val
                value_to_node[node.right.val] = node.right
                queue.append(node.right)

        # Find ancestors of p
        ancestors_of_p = set()
        current = p.val
        while current is not None:
            ancestors_of_p.add(current)
            current = parent_dict[current]

        # Check ancestors of q
        current = q.val
        while current is not None:
            if current in ancestors_of_p:
                return value_to_node[current]
            current = parent_dict[current]

        return None

#
# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)

solution = Solution()
p = root.left.right
q = root.left.left.left
print("p,", p.val)
print("q,", q.val)
print("lca bfs",solution.lowestCommonAncestorBFS(root, p, q).val)
print("lca dfs",solution.lowestCommonAncestor(root, p, q).val)
